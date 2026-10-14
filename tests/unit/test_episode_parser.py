"""Tests for series, special, and absolute-anime parsing."""

from media_organizer.naming import (
    absolute_episode_filename,
    season_directory,
    series_episode_filename,
)
from media_organizer.parser import parse_episode_filename


def test_parses_series_episode_and_proposed_name() -> None:
    result = parse_episode_filename(
        "Jujutsu.Kaisen.S02E04.1080p.BluRay.Opus2.0.x265.DUAL-Anitsu.mkv"
    )

    assert result.title == "Jujutsu Kaisen"
    assert result.season == 2
    assert result.episodes == (4,)
    assert result.extension == ".mkv"
    assert not result.review_required
    assert series_episode_filename(result.title, result.season, result.episodes, result.extension) == (
        "S02E04 - Jujutsu Kaisen.mkv"
    )


def test_parses_multiple_episodes() -> None:
    result = parse_episode_filename("Show.S01E01E02.1080p.mkv")

    assert result.title == "Show"
    assert result.season == 1
    assert result.episodes == (1, 2)
    assert series_episode_filename(result.title, result.season, result.episodes, result.extension) == (
        "S01E01-E02 - Show.mkv"
    )


def test_parses_specials_into_specials_directory() -> None:
    result = parse_episode_filename("Show.S00E01.1080p.mkv")

    assert result.title == "Show"
    assert result.season == 0
    assert result.episodes == (1,)
    assert season_directory(result.season) == "Especiais"
    assert series_episode_filename(result.title, result.season, result.episodes, result.extension) == (
        "S00E01 - Show.mkv"
    )


def test_parses_absolute_anime_when_title_is_a_strong_signal() -> None:
    result = parse_episode_filename("One.Piece.1123.1080p.WEB-DL.mkv")

    assert result.title == "One Piece"
    assert result.absolute_episode == 1123
    assert not result.review_required
    assert absolute_episode_filename(result.title, result.absolute_episode, result.extension) == (
        "1123 - One Piece.mkv"
    )


def test_ambiguous_absolute_number_requires_review() -> None:
    result = parse_episode_filename("Show.1123.1080p.WEB-DL.mkv")

    assert result.absolute_episode == 1123
    assert result.review_required


def test_unknown_episode_shape_requires_review() -> None:
    result = parse_episode_filename("Jujutsu.Kaisen.S02.1080p.BluRay.mkv")

    assert result.review_required
