"""Schema parsing utilities"""
import re
from typing import Optional

from pydantic import NonNegativeInt

from bids_pydantic.version_info import SchemaVersion
from bids_pydantic.version_specific_changes import fix_yaml_str

# This is to be inserted into the BIDS metadata YAML file to allow it to be
# recognised as a JSON schema
YAML_HEADER_BLOCK = (
    """
$schema: "https://json-schema.org/draft/2020-12/schema"
title: BIDS metadata
description: |
  This schema contains definitions for all metadata fields (fields which may"""
    """  appear in sidecar JSON files) currently supported in BIDS.
type: object
properties:
"""
)


def find_first_non_comment_line(yaml_str: str) -> Optional[NonNegativeInt]:
    """Find the first (non-empty/whitespace) line that does not have any comments in.
    Returns the line number (starting from 0) or None

    :param yaml_str: The full, multiline YAML string
    :return: The line number of the first line that does not have comments in, or
    None if it cannot be found."""

    for line_number, line in enumerate(yaml_str.splitlines()):
        match = re.match(r"^\s*(?!---)[^#\s].*$", line, re.DOTALL)
        if match:
            return line_number

    return None


def indent_all_lines(
    yaml_str: str, from_line: NonNegativeInt = 0, indent: NonNegativeInt = 2
) -> str:
    """Indents all lines (by 2) from, and including line `from_line`.
    Returns the indented text

    :param yaml_str: The full, multiline YAML string
    :param from_line: The line to start indenting from
    :param indent: The size of the indent

    :return: The indented, multiline YAML string"""

    indent_str = "".join(" " for _ in range(indent))
    return "\n".join(
        line if line_number < from_line else indent_str + line
        for line_number, line in enumerate(yaml_str.splitlines())
    )


def adjust_references(yaml_str: str) -> str:
    """Changes all `$ref: something` to `$ref: #/something` to allow JSON
    schema parsing

    :param yaml_str: The full, multiline YAML string

    :return: The full, multiline YAML string with references adjusted"""
    return re.sub(r"^(\s*-?\s*\$ref:\s*)(.+)", r"\1#/\2", yaml_str, flags=re.MULTILINE)


def insert_yaml_header(yaml_str: str) -> Optional[str]:
    """Insert the :py:attr:YAML_HEADER_BLOCK into the YAML data at the appropriate
    position

    :param yaml_str: The full, multiline YAML string

    :return: The full, multiline YAML string with the YAML header inserted"""
    line_number = find_first_non_comment_line(yaml_str)
    if line_number is None:
        return None

    return (
        "\n".join(line for line in yaml_str.splitlines()[:line_number])
        + YAML_HEADER_BLOCK
        + "\n".join(line for line in yaml_str.splitlines()[line_number:])
    )


def prepare_yaml_metadata_text(
    yaml_str: str, version: Optional[SchemaVersion] = None
) -> Optional[str]:
    """The downloaded YAML will not convert directly to a valid JSON (YAML) schema.
    Some changes need to be made to the text before it can be parsed by
    datamodel_code_generator into pydantic models.
    This function fixed any version-specific errors in the YAML schema,
    adds top-level schema information, wraps all attributes into
    a single object, and converts variables so they are JSON schema-addressable.

    :param yaml_str: The full, multiline YAML string
    :param version: The version of the schema that is being converted

    :return: The full, multiline YAML string which can be parsed by
    datamodel_code_generator"""

    # Find the first non-comment line
    insert_line_number = find_first_non_comment_line(yaml_str)
    if insert_line_number is None:
        return None

    return insert_yaml_header(
        indent_all_lines(
            adjust_references(
                yaml_str
                if version is None
                else fix_yaml_str(input_str=yaml_str, version=version)
            ),
            from_line=insert_line_number,
        )
    )
