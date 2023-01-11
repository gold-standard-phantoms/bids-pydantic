"""Setup for BIDS-pydantic-models"""
import os
import re

from setuptools import find_packages, setup

with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()


def read(rel_path: str) -> str:
    """Reads in a file, relative to this one
    :param rel_path: the relative path to read
    :return: the file contents, as a string
    """
    here = os.path.abspath(os.path.dirname(__file__))
    # intentionally *not* adding an encoding option to open, See:
    #   https://github.com/pypa/virtualenv/issues/201#issuecomment-3145690
    with open(  # pylint: disable=unspecified-encoding
        os.path.join(here, rel_path)
    ) as file_obj:
        return file_obj.read()


def check_semver(version_string: str) -> bool:
    """Check a given string is in semver format
    :return: True if in correct format, otherwise False
    """
    semver_pattern = (
        r"^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\."
        r"(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*"
        r"[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
        r"(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
    )
    return re.match(semver_pattern, version_string) is not None


def get_version(rel_path: str) -> str:
    """Get the version from the file specified by the
    relative path. This reads the text directly, rather
    than importing the file. Will use variables from
    Gitlab-CI to add suffixes to the version
    :param rel_path: the relative path to read
    :return: the version string in semver e.g. 0.1.3, 0.1.3-dev-ea99db65
    :raises: RuntimeError if the version is not found, or it
    is not in semver format
    """

    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            project_version = line.split(delim)[1]
            if not check_semver(project_version):
                raise RuntimeError(
                    f"Version: {project_version} is not in semver format"
                )
            branch: str = os.environ.get("CI_COMMIT_BRANCH", "unknown")
            ci_pipeline_iid: str = os.environ.get("CI_PIPELINE_IID", "unknown")
            ci_commit_short_sha: str = os.environ.get("CI_COMMIT_SHORT_SHA", "unknown")

            if branch.lower() in ["dev", "develop", "development"]:
                return f"{project_version}.dev{ci_pipeline_iid}+{ci_commit_short_sha}"

            # Return the semver for master branch
            if branch.lower() in ["master", "main", "release"]:
                return project_version

            # otherwise return the version, branch name and commit hash
            # this should never occur in non-protected (main/dev) branches on CI/CD.
            return f"{project_version}+{branch}.{ci_commit_short_sha}"
    raise RuntimeError("Unable to find version string.")


setup(
    name="BIDS-pydantic-models",
    version=get_version("../src/bids_pydantic/__init__.py"),
    author="Gold Standard Phantoms",
    author_email="tom.hampshire@goldstandardphantoms.com",
    description="Pydantic models for BIDS metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/gold-standard-phantoms/bids-pydantic",
    project_urls={
        "Documentation": "https://github.com/gold-standard-phantoms/bids-pydantic",
        "Code": "https://github.com/gold-standard-phantoms/bids-pydantic",
        "Issue tracker": (
            "https://github.com/gold-standard-phantoms/bids-pydantic/issues"
        ),
    },
    package_dir={"": "src"},
    packages=["bids_pydantic_models"],
    package_data={
        "bids_pydantic_models": ["py.typed"],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=requirements,
    include_package_data=True,
)
