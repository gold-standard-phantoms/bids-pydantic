"""Classes and variables used for versioning/version information"""
import re
from functools import total_ordering
from typing import Any, Final, Generic, Optional, Type, TypeVar

from pydantic import Field, NonNegativeInt
from pydantic.generics import GenericModel

from bids_pydantic import __version__

# A bound Semver type for generics
SemverType = TypeVar("SemverType", bound="Semver")


@total_ordering
class Semver(GenericModel, Generic[SemverType]):
    """A semver represention i.e. vX.Y.Z"""

    major: NonNegativeInt = Field(...)
    """The major version number"""

    minor: NonNegativeInt = Field(...)
    """The minor version number"""

    patch: NonNegativeInt = Field(...)
    """The patch version number"""

    @classmethod
    def from_string(cls: Type[SemverType], semver_str: str) -> Optional[SemverType]:
        """Converts from the following string formats:
        X.Y.Z
        vX.Y.Z
        VX.Y.Z
        """
        result = re.search(r"^[vV]?([0-9]+)\.([0-9]+)\.([0-9]+)$", semver_str)
        if result is None:
            return None
        major, minor, patch = result.groups()
        return cls(major=int(major), minor=int(minor), patch=int(patch))

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Semver):
            raise NotImplementedError()
        return all(
            getattr(self, label) == getattr(other, label)
            for label in ["major", "minor", "patch"]
        )

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Semver):
            raise NotImplementedError()
        for label in ["major", "minor", "patch"]:
            if getattr(self, label) == getattr(other, label):
                continue
            if getattr(self, label) < getattr(other, label):
                return True
            if getattr(self, label) > getattr(other, label):
                return False
        return False

    def __repr__(self) -> str:
        return f"v{self.major}.{self.minor}.{self.patch}"

    def __str__(self) -> str:
        """Representation of the semver"""
        return self.__repr__()


class SchemaVersion(Semver["SchemaVersion"]):
    """A BIDS schema version represention"""

    def get_schema_url(self) -> str:
        """Return the YAML BIDS schema URL for the schema version"""
        return (
            "https://raw.githubusercontent.com/bids-standard/bids-specification/"
            f"v{self.major}.{self.minor}.{self.patch}/"
            "src/schema/objects/metadata.yaml"
        )


# Do not support below this version
MIN_SUPPORTED_SCHEMA_VERSION: Final[SchemaVersion] = SchemaVersion(
    major=1, minor=7, patch=0
)

# Not tested above this version
MAX_TESTED_SCHEMA_VERSION: Final[SchemaVersion] = SchemaVersion(
    major=1, minor=7, patch=0
)


def is_supported_version(version: Semver) -> bool:
    """Determine if the version of the BIDS specification is supported.
    Currently, we assume that v1.7.0 and up is going to be supported, but this may
    need revising in the future"""
    return version >= Semver(major=1, minor=7, patch=0)
