"""Windows-safe component sanitization."""

import re

_INVALID_CHARACTERS = re.compile(r'[\\/:*?"<>|]')
_WHITESPACE = re.compile(r"\s+")
_DUPLICATE_HYPHENS = re.compile(r"-{2,}")
_RESERVED_NAMES = {"AUX", "CON", "NUL", "PRN", *(f"COM{i}" for i in range(1, 10)), *(f"LPT{i}" for i in range(1, 10))}


def sanitize_component(value: str) -> str:
    """Return a deterministic Windows-safe path component.

    This function only transforms text. It never reads or changes the filesystem.
    """
    sanitized = _INVALID_CHARACTERS.sub("-", value)
    sanitized = _WHITESPACE.sub(" ", sanitized).strip()
    sanitized = _DUPLICATE_HYPHENS.sub("-", sanitized)
    sanitized = re.sub(r"(?<=\w)-(?=\s)", " -", sanitized)
    sanitized = re.sub(r"(?<=\s)-(?=\w)", "- ", sanitized).strip(" .")

    if not sanitized:
        return "Untitled"

    if sanitized.upper().split(".", 1)[0] in _RESERVED_NAMES:
        sanitized = f"{sanitized} -"

    return sanitized
