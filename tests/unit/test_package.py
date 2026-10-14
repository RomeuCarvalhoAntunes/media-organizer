"""Bootstrap sanity checks for the Python package."""

from media_organizer import __version__


def test_package_is_importable() -> None:
    """The package exposes a version and can be imported by the test runner."""
    assert __version__ == "0.1.0"
