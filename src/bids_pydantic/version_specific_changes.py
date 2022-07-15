"""Makes changes to BIDS schema yaml file based on the version (if necessary)"""

from typing import Callable, Dict

from bids_pydantic.version_info import SchemaVersion


def patch_v1_7_0(input_str: str) -> str:
    """Account for
    https://github.com/bids-standard/bids-specification/issues/1156"""
    split = input_str.splitlines()
    assert split[373] == "  items:"
    assert split[375] == "    minItems: 2"
    assert split[376] == "    maxItems: 3"
    return "\n".join(
        split[:373] + ["  minItems: 2", "  maxItems: 3"] + split[373:375] + split[377:]
    )


SCHEMA_FUNCS: Dict[SchemaVersion, Callable[[str], str]] = {
    SchemaVersion(major=1, minor=7, patch=0): patch_v1_7_0
}


def fix_yaml_str(input_str: str, version: SchemaVersion) -> str:
    """Perform version-specific adjustments to input YAML (e.g. for bugfixes)"""
    if version in SCHEMA_FUNCS:
        return SCHEMA_FUNCS[version](input_str)
    return input_str
