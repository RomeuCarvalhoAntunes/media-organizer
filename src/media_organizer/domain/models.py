"""Small, dependency-free domain models for media identities."""

from dataclasses import dataclass
from enum import Enum


class MediaKind(str, Enum):
    """Kinds of media recognized by the naming layer."""

    MOVIE = "movie"
    SERIES_EPISODE = "series_episode"
    SPECIAL = "special"
    ABSOLUTE_EPISODE = "absolute_episode"
    SUBTITLE = "subtitle"


class ItemState(str, Enum):
    """Possible outcomes for an item in the organization workflow."""

    READY = "READY"
    UNCHANGED = "UNCHANGED"
    POSSIBLE_DUPLICATE = "POSSIBLE_DUPLICATE"
    CONFLICT = "CONFLICT"
    IGNORED = "IGNORED"
    REVIEW_REQUIRED = "REVIEW_REQUIRED"
    ERROR = "ERROR"


@dataclass(frozen=True)
class MediaItem:
    """A parsed media identity, without any filesystem behavior."""

    title: str
    kind: MediaKind
    extension: str
    season: int | None = None
    episodes: tuple[int, ...] = ()
    absolute_episode: int | None = None
    subtitle_language: str | None = None
    subtitle_qualifiers: tuple[str, ...] = ()
