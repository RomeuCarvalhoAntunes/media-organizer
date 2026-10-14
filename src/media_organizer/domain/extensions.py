"""Supported media filename extensions."""

VIDEO_EXTENSIONS = frozenset({".avi", ".m4v", ".mkv", ".mov", ".mp4", ".mpeg", ".webm"})
SUBTITLE_EXTENSIONS = frozenset({".ass", ".idx", ".srt", ".ssa", ".sub", ".sup"})


def is_supported_video_extension(extension: str) -> bool:
    """Return whether an extension identifies a supported video file."""
    return extension.lower() in VIDEO_EXTENSIONS


def is_supported_subtitle_extension(extension: str) -> bool:
    """Return whether an extension identifies a supported subtitle file."""
    return extension.lower() in SUBTITLE_EXTENSIONS
