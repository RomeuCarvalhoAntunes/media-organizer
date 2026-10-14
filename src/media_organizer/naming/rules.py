"""Naming rules for movies, series, episodes, and subtitles."""

from collections.abc import Iterable

from media_organizer.naming.sanitize import sanitize_component


def _extension(extension: str) -> str:
    """Normalize an extension while preserving the caller's actual suffix."""
    return extension if extension.startswith(".") else f".{extension}"


def movie_directory(title: str) -> str:
    """Return the final directory name for a movie."""
    return sanitize_component(title)


def movie_filename(title: str, extension: str) -> str:
    """Return the final filename for a movie."""
    return f"{sanitize_component(title)}{_extension(extension)}"


def series_directory(title: str) -> str:
    """Return the final top-level directory name for a series."""
    return sanitize_component(title)


def season_directory(season: int) -> str:
    """Return the final directory name for a season or specials."""
    if season < 0:
        raise ValueError("season cannot be negative")
    return "Especiais" if season == 0 else f"{season}ª - Temporada"


def series_episode_filename(
    title: str,
    season: int,
    episodes: Iterable[int],
    extension: str,
) -> str:
    """Return a filename for a normal or multi-episode release."""
    episode_numbers = tuple(episodes)
    if season < 0 or not episode_numbers or any(episode < 0 for episode in episode_numbers):
        raise ValueError("season and episodes must be non-negative and non-empty")

    episode_label = f"S{season:02d}E{episode_numbers[0]:02d}"
    if len(episode_numbers) > 1:
        episode_label += "-" + "-".join(f"E{episode:02d}" for episode in episode_numbers[1:])
    return f"{episode_label} - {sanitize_component(title)}{_extension(extension)}"


def absolute_episode_filename(title: str, episode: int, extension: str) -> str:
    """Return a filename for an anime using absolute episode numbering."""
    if episode < 0:
        raise ValueError("episode cannot be negative")
    return f"{episode} - {sanitize_component(title)}{_extension(extension)}"


def subtitle_filename(
    video_basename: str,
    extension: str,
    language: str | None = None,
    qualifiers: Iterable[str] = (),
) -> str:
    """Return a subtitle filename compatible with a video's basename."""
    parts = [sanitize_component(video_basename)]
    if language:
        parts.append(sanitize_component(language))
    parts.extend(sanitize_component(qualifier) for qualifier in qualifiers if qualifier)
    return f"{'.'.join(parts)}{_extension(extension)}"
