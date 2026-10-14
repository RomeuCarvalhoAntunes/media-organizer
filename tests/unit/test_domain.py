"""Tests for the pure domain and naming layer."""

import pytest

from media_organizer.domain.extensions import (
    is_supported_subtitle_extension,
    is_supported_video_extension,
)
from media_organizer.domain.models import ItemState, MediaItem, MediaKind
from media_organizer.naming import (
    absolute_episode_filename,
    movie_directory,
    movie_filename,
    sanitize_component,
    season_directory,
    series_directory,
    series_episode_filename,
    subtitle_filename,
)


def test_domain_models_cover_alfa_states_and_identities() -> None:
    item = MediaItem("One Piece", MediaKind.ABSOLUTE_EPISODE, ".mkv", absolute_episode=1123)

    assert item.kind is MediaKind.ABSOLUTE_EPISODE
    assert item.absolute_episode == 1123
    assert {state.value for state in ItemState} == {
        "READY",
        "UNCHANGED",
        "POSSIBLE_DUPLICATE",
        "CONFLICT",
        "IGNORED",
        "REVIEW_REQUIRED",
        "ERROR",
    }


@pytest.mark.parametrize("extension", [".mkv", ".MP4", ".webm"])
def test_supported_video_extensions_are_case_insensitive(extension: str) -> None:
    assert is_supported_video_extension(extension)


@pytest.mark.parametrize("extension", [".srt", ".ASS", ".sup"])
def test_supported_subtitle_extensions_are_case_insensitive(extension: str) -> None:
    assert is_supported_subtitle_extension(extension)


def test_unsupported_extensions_are_rejected() -> None:
    assert not is_supported_video_extension(".jpg")
    assert not is_supported_subtitle_extension(".nfo")


def test_sanitize_windows_invalid_characters_and_spacing() -> None:
    assert sanitize_component("John Wick 4: Baba Yaga") == "John Wick 4 - Baba Yaga"
    assert sanitize_component("  A---  Title... ") == "A - Title"


@pytest.mark.parametrize("reserved", ["CON", "con.txt", "LPT1"])
def test_sanitize_windows_reserved_names(reserved: str) -> None:
    assert sanitize_component(reserved).endswith(" -")


def test_sanitize_empty_name() -> None:
    assert sanitize_component("...   ") == "Untitled"


def test_movie_naming() -> None:
    assert movie_directory("John Wick Chapter 4") == "John Wick Chapter 4"
    assert movie_filename("John Wick Chapter 4", "mkv") == "John Wick Chapter 4.mkv"


def test_series_naming() -> None:
    assert series_directory("Jujutsu Kaisen") == "Jujutsu Kaisen"
    assert season_directory(2) == "2ª - Temporada"
    assert series_episode_filename("Jujutsu Kaisen", 2, [4], ".mkv") == (
        "S02E04 - Jujutsu Kaisen.mkv"
    )


def test_multiple_episode_naming() -> None:
    assert series_episode_filename("Show", 1, [1, 2], ".mkv") == "S01E01-E02 - Show.mkv"


def test_special_naming() -> None:
    assert season_directory(0) == "Especiais"
    assert series_episode_filename("Show", 0, [1], ".mkv") == "S00E01 - Show.mkv"


def test_absolute_anime_naming() -> None:
    assert absolute_episode_filename("One Piece", 1123, ".mkv") == "1123 - One Piece.mkv"


def test_subtitle_naming() -> None:
    assert subtitle_filename("A Favorita", ".srt") == "A Favorita.srt"
    assert subtitle_filename("A Favorita", ".srt", "pt-BR", ["forced"]) == (
        "A Favorita.pt-BR.forced.srt"
    )
