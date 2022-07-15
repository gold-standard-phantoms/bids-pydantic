"""A utility to download a BIDS metadata schema and generate
corresponding pydantic models"""

from __future__ import annotations

import json
import logging
import os.path
import re
import urllib.request
from os import PathLike
from tempfile import TemporaryDirectory
from typing import Any, Final, List, Optional, Union

from datamodel_code_generator.__main__ import main as code_generator_main
from datamodel_code_generator.version import version as datamodel_code_generator_version
from pydantic import BaseModel, Field, validator

from bids_pydantic import __version__
from bids_pydantic.schema_parsing import (
    find_first_non_comment_line,
    prepare_yaml_metadata_text,
)
from bids_pydantic.version_info import SchemaVersion, Semver, is_supported_version

# The bids-specification repo tags information API endpoint
API_URL: Final[
    str
] = "https://api.github.com/repos/bids-standard/bids-specification/git/refs/tags"


class Ref(BaseModel):
    """An API reference. A list of these are returned from :py:const:`API_URL`"""

    ref: str = Field(...)

    def get_version(self) -> Optional[Semver]:
        """Get a Semver with the version information. Returns None if
        the version information cannot be parsed."""
        result = re.search(r"^refs/tags/(.*)$", self.ref)
        if result is None:
            return None
        return Semver.from_string(result.groups()[0])


class ApiResponse(BaseModel):
    """A direct response from the :py:const:`API_URL`"""

    response: List[Ref] = Field(...)

    @staticmethod
    def load_from_api() -> ApiResponse:
        """Load the ApiResponse from the GitHub API :py:const:`API_URL`"""
        with urllib.request.urlopen(API_URL) as file_obj:
            return ApiResponse(response=json.loads(file_obj.read().decode("utf-8")))

    def get_versions(self) -> List[Semver]:
        """List the (sorted) BIDS versions"""
        return sorted(
            version
            for version in (ref.get_version() for ref in self.response)
            if version is not None
        )

    def get_supported_versions(self) -> List[Semver]:
        """List the (sorted) supported BIDS versions.
        See :py:func:`is_supported_version` for more information"""
        return [
            version for version in self.get_versions() if is_supported_version(version)
        ]


def is_file_writable(filename: str) -> bool:
    """Is a file with the given filename writable.
    The file does not have to exist.

    :param filename: the filename to check

    :return True if a file with the filename can be written to"""
    if os.path.exists(filename):
        # path exists
        if os.path.isfile(filename):  # is it a file or a dir?
            # also works when file is a link and the target is writable
            return os.access(filename, os.W_OK)
        return False  # path is a dir, so cannot write as a file
    # target does not exist, check perms on parent dir
    pdir = os.path.dirname(filename)
    if not pdir:
        pdir = "."
    # target is creatable if parent dir is writable
    return os.access(pdir, os.W_OK)


class ConvertParams(BaseModel):
    """Parameters for making BIDS-compliant pydantic models given a BIDS schema
    version number"""

    schema_version_or_path: Union[SchemaVersion, PathLike]
    """The schema to use. Either a version number or a file to the schema."""

    @validator("schema_version_or_path")
    def if_file_must_exist(cls, value: Any) -> Union[SchemaVersion, PathLike]:
        """Check we have a schema or is an existing file"""
        if isinstance(value, SchemaVersion):
            return value
        if isinstance(value, PathLike):
            # The file must exist and be a file
            if os.path.exists(value) and os.path.isfile(value):
                return value
            raise ValueError(f"{value} is not an existing file")
        raise ValueError("{value} is not a valid input")

    output_filename: str
    """The (python) filename to output the models to"""

    @validator("output_filename")
    def validate_output_filename(cls, value: Any) -> str:
        """Check the file can be written to"""
        if not isinstance(value, str):
            raise TypeError("output_filename must be a string")
        if not is_file_writable(value):
            raise ValueError(f"File {value} is not writable")
        return value

    class Config:
        """ConvertParams config"""

        arbitrary_types_allowed = True  # needed for PathLike


def create_models(params: ConvertParams) -> None:
    """Create the pydantic models at the given filename using the provided schema
    version

    :param params: The input parameters"""
    yaml_str: Optional[str]

    # If the params specify a version of the schema, download it
    if isinstance(params.schema_version_or_path, SchemaVersion):
        logging.info(
            "Downloading BIDS schema version %s", params.schema_version_or_path
        )
        with urllib.request.urlopen(
            params.schema_version_or_path.get_schema_url()
        ) as file_obj:
            yaml_str = file_obj.read().decode("utf-8")
    else:
        logging.info("Opening BIDS schema from %s", params.schema_version_or_path)
        with open(params.schema_version_or_path, encoding="utf-8") as file_obj:
            yaml_str = file_obj.read()

    if yaml_str is None:
        raise ValueError("Schema could not be successfully read")
    # Prepare the yaml data for conversion - apply any version-specific adjustments
    yaml_str = prepare_yaml_metadata_text(
        yaml_str=yaml_str,
        version=params.schema_version_or_path
        if isinstance(params.schema_version_or_path, SchemaVersion)
        else None,
    )
    if yaml_str is None:
        raise ValueError("Input YAML could not be successfully parsed")

    # Write the yaml file to a temp directory so we can easy load it into
    # datamodel_code_generator
    with TemporaryDirectory() as temp_dir:
        yaml_filename = os.path.join(temp_dir, "schema.yaml")
        with open(yaml_filename, "w", encoding="utf-8") as file_obj:
            file_obj.write(yaml_str)

        # For now, just use the default parameters
        code_generator_main(
            args=[
                # for nicer formatting"
                "--wrap-string-literal",
                # Use schema description to populate class docstring
                "--use-schema-description",
                "--input",
                yaml_filename,
                "--output",
                params.output_filename,
            ]
        )
        # Add some version information to the generated file
        data: str
        with open(params.output_filename, encoding="utf-8") as original:
            data = original.read()

        # String leading comments
        first_non_comment_line = find_first_non_comment_line(data)
        if first_non_comment_line is None:
            raise ValueError("Created .py data does not have any code")

        data = "\n".join(
            line
            for line_number, line in enumerate(data.splitlines())
            if line_number >= first_non_comment_line
        )

        with open(params.output_filename, "w", encoding="utf-8") as modified:
            modified.write(
                f"# Generated using BIDS-pydantic v{__version__} "
                f"using BIDS schema {params.schema_version_or_path}\n"
            )
            if isinstance(params.schema_version_or_path, SchemaVersion):
                modified.write(
                    f"# from {params.schema_version_or_path.get_schema_url()}\n"
                )
            modified.write(
                "# Uses datamodel-code-generator "
                f"v{datamodel_code_generator_version}\n" + data
            )
