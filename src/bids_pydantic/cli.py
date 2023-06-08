"""BIDS-pydantic command line interface"""
import argparse
import logging
import os
import sys
from enum import Enum
from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import Final, Union

from bids_pydantic.bids_model_generator import (
    ApiResponse,
    ConvertParams,
    SchemaVersion,
    create_models,
)
from bids_pydantic.version_info import (
    MAX_TESTED_SCHEMA_VERSION,
    MIN_SUPPORTED_SCHEMA_VERSION,
)

# The name of the command that was run
THIS: Final[str] = os.path.basename(sys.argv[0])

# Set up logging
FORMAT: Final[str] = "%(levelname)s: %(message)s"
logging.basicConfig(format=FORMAT)
logging.getLogger().setLevel(logging.INFO)


class Commands(str, Enum):
    """Supported CLI commands"""

    LIST = "list"
    MAKE = "make"


def list_commands() -> None:
    """Evaluate the `list` command. Exits the program."""
    supported_versions = ApiResponse.load_from_api().get_supported_versions()
    print(
        "Supported versions: "
        f"{', '.join(str(version) for version in supported_versions)}"
    )
    sys.exit(0)


def make_commands(args: argparse.Namespace) -> None:
    """Evaluate the `make` command. Exits the program."""
    if args.output is not None and args.output_all is not None:
        logging.error("Cannot use --output with --output-all")
        sys.exit(1)

    if args.schema_version is not None and args.input is not None:
        logging.error("Cannot use --schema-version with --input")
        sys.exit(1)

    if args.schema_version is not None and args.output_all is not None:
        logging.error("Cannot use --schema-version with --output_all")
        sys.exit(1)

    schema: Union[SchemaVersion, os.PathLike, None] = None

    if args.schema_version is not None:
        # A schema version has been specified
        schema = get_schema_version(args.schema_version)
    elif args.input is not None:
        # An input filename has been specified
        schema = Path(args.input)
    else:
        # Use the default schema
        schema = MAX_TESTED_SCHEMA_VERSION

    # If an output filename has been specified
    if args.output is not None:
        convert_params = ConvertParams(
            schema_version_or_path=schema, output_filename=args.output
        )
        create_models(convert_params)
        sys.exit(0)

    supported_versions = ApiResponse.load_from_api().get_supported_versions()
    # If we should output all possible versions of the schema
    if args.output_all is not None:
        logging.info(
            "Outputting all parsable versions of the BIDS schema as a pydantic model"
        )
        for supported_version in supported_versions:
            output_filename = os.path.join(
                args.output_all,
                "bids_metadata_" + str(supported_version).replace(".", "_") + ".py",
            )
            logging.info("Creating %s", output_filename)

            convert_params = ConvertParams(
                schema_version_or_path=supported_version,
                output_filename=output_filename,
            )
            create_models(convert_params)
        sys.exit(0)

    # If an output filename has not been specified
    with NamedTemporaryFile("w", encoding="utf-8") as temp_file:
        convert_params = ConvertParams(
            schema_version_or_path=schema, output_filename=temp_file.name
        )
        create_models(convert_params)
        temp_file.flush()
        temp_file.seek(0)
        with open(temp_file.name, encoding="utf-8") as file:
            print(file.read())

    sys.exit(0)


def main() -> None:
    """Main function"""
    # add cli completion support
    parser = argparse.ArgumentParser(
        description=f"""Run one of a set of commands. For example:
        `{THIS} list`,
        or `{THIS} make`.
        Run either command with `-h` e.g.
        `{THIS} {Commands.MAKE} -h` to get help for that command."""
    )

    subparsers = parser.add_subparsers(
        title="command", help="subcommand to run", dest="command"
    )

    # `list` subparser
    subparsers.add_parser(
        name="list",
        description=f"""Queries the GitHub API and lists the
        available supported BIDS schema versions.
        Only tested up to {MAX_TESTED_SCHEMA_VERSION}.""",
    )

    make_parser = subparsers.add_parser(
        name="make",
        description=(
            "Make a new python file(s) containing BIDS compliant pydantic models"
        ),
    )

    make_parser.add_argument(
        "--output",
        "-o",
        help=(
            "The output python filename to create (will output to stdout "
            "console if not specified)."
        ),
        type=str,
    )

    make_parser.add_argument(
        "--output-all",
        "-a",
        help=(
            "Find all parsable schemas and output each to the provided directory. "
            "Will create filenames such as bids_schema_model_v_1_7_0.py, etc. "
            "Will overwrite any files in that directory with the same name."
        ),
        type=str,
    )
    make_parser.add_argument(
        "--schema-version",
        help=f"""The BIDS schema version to use. e.g. 1.7.0 -
        supported versions can be discovered using the list command.
        If a version is not specified {MAX_TESTED_SCHEMA_VERSION} will be used.""",
        type=str,
    )

    make_parser.add_argument(
        "--input",
        "-i",
        help=(
            "Specify an input BIDS metadata (yml) file to use instead of downloading a"
            " version from GitHub. Cannot be used with --schema-version or --output-all"
        ),
        type=str,
    )

    args = parser.parse_args()
    if args.command == Commands.LIST:
        list_commands()
    if args.command == Commands.MAKE:
        make_commands(args)

    parser.print_help()


def get_schema_version(schema_version: str) -> SchemaVersion:
    """Checks whether the given schema version string is valid, supported
    and exists on the BIDS-standard GitHub repository. Returns the `SchemaVersion` if
    all are True."""
    supported_versions = ApiResponse.load_from_api().get_supported_versions()
    schema = SchemaVersion.from_string(schema_version)
    if schema is None:
        logging.error("%s not a valid version", schema_version)
        sys.exit(1)
    if schema < MIN_SUPPORTED_SCHEMA_VERSION:
        logging.error(
            (
                "This version of the schema %s cannot be converted. "
                "Please use %s or greater."
            ),
            schema,
            MIN_SUPPORTED_SCHEMA_VERSION,
        )
        sys.exit(1)

    if schema not in supported_versions:
        logging.error("Version %s is not available for download", schema)
        sys.exit(1)
    if schema > MAX_TESTED_SCHEMA_VERSION:
        logging.warning(
            (
                "Warning - this version % of the schema has "
                "been untested with this converter."
            ),
            schema,
        )
    return schema


if __name__ == "__main__":
    main()
