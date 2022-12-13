"""BIDS model generator tests"""
from bids_pydantic.bids_model_generator import ApiResponse, Semver


def test_semver_eq() -> None:
    """Test semver equality"""
    assert Semver(major=1, minor=2, patch=3) == Semver(major=1, minor=2, patch=3)
    assert Semver(major=1, minor=2, patch=4) != Semver(major=1, minor=2, patch=3)
    assert Semver(major=1, minor=1, patch=3) != Semver(major=1, minor=2, patch=3)
    assert Semver(major=4, minor=2, patch=3) != Semver(major=1, minor=2, patch=3)


def test_semver_lt() -> None:
    """Test semver gt, le, etc"""
    assert Semver(major=1, minor=2, patch=3) >= Semver(major=1, minor=2, patch=3)
    assert Semver(major=1, minor=2, patch=4) > Semver(major=1, minor=2, patch=3)
    assert Semver(major=1, minor=1, patch=3) < Semver(major=1, minor=2, patch=3)
    assert Semver(major=0, minor=2, patch=3) < Semver(major=1, minor=2, patch=3)
    assert Semver(major=1, minor=2, patch=2) < Semver(major=1, minor=2, patch=3)


def test_api_response() -> None:
    """Test a realistic response from the GitHub api is parsed correctly"""
    response = [
        {
            "ref": "refs/tags/v1.1.2",
            "node_id": "MDM6UmVmMTUwNDY1MjM3OnJlZnMvdGFncy92MS4xLjI=",
            "url": (
                "https://api.github.com/repos/bids-standard/"
                "bids-specification/git/refs/tags/v1.1.2"
            ),
            "object": {
                "sha": "2e49d8e6f37f343d46cb28120794011c89def5cf",
                "type": "tag",
                "url": (
                    "https://api.github.com/repos/bids-standard/"
                    "bids-specification/git/tags/2e49d8e6f37f343d46cb28120794011c89def5cf"
                ),
            },
        },
        {
            "ref": "refs/tags/v99.88.77",
            "node_id": "MDM6UmVmMTUwNDY1MjM3OnJlZnMvdGFncy92MS4yLjA=",
            "url": (
                "https://api.github.com/repos/bids-standard/"
                "bids-specification/git/refs/tags/v99.88.77"
            ),
            "object": {
                "sha": "584a8e256eff0069ecfb72f29b392e9c64b14f89",
                "type": "tag",
                "url": (
                    "https://api.github.com/repos/bids-standard/"
                    "bids-specification/git/tags/584a8e256eff0069ecfb72f29b392e9c64b14f89"
                ),
            },
        },
    ]
    parsed = ApiResponse(response=response)
    assert len(parsed.response)
    assert parsed.response[0].get_version() == Semver(major=1, minor=1, patch=2)
    assert parsed.response[1].get_version() == Semver(major=99, minor=88, patch=77)


def test_get_supported_version() -> None:
    """Check that correctly supported BIDS versions ONLY are returned (and sorted)"""
    # Don't include the ignored fields
    response = [
        {"ref": "refs/tags/v1.1.0"},  # unsupported
        {"ref": "refs/tags/v42.3.0"},  # supported
        {"ref": "refs/tags/v3.1.4"},  # supported
        {"ref": "refs/tags/v2.0.0"},  # supported
        {"ref": "refs/tags/v1.8.0"},  # supported
        {"ref": "refs/tags/v1.7.1"},  # supported
        {"ref": "refs/tags/v1.7.0"},  # supported
        {"ref": "refs/tags/v0.1.4"},  # unsupported
    ]
    parsed = ApiResponse(response=response)
    assert parsed.get_supported_versions() == [
        Semver(major=1, minor=7, patch=0),
        Semver(major=1, minor=7, patch=1),
        Semver(major=1, minor=8, patch=0),
        Semver(major=2, minor=0, patch=0),
        Semver(major=3, minor=1, patch=4),
        Semver(major=42, minor=3, patch=0),
    ]


def test_semver_from_string() -> None:
    """Check that semvers are created correctly from strings"""
    assert Semver.from_string("13.2.34") == Semver(major=13, minor=2, patch=34)
    assert Semver.from_string("v1.23.344") == Semver(major=1, minor=23, patch=344)
    assert Semver.from_string("V2.0.1") == Semver(major=2, minor=0, patch=1)
