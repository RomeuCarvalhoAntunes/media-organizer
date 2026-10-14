"""Tests for conservative movie release parsing."""

from media_organizer.parser import parse_movie_filename


def test_parses_john_wick_release() -> None:
    result = parse_movie_filename(
        "John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv"
    )

    assert result.title == "John Wick Chapter 4"
    assert result.year == 2023
    assert result.extension == ".mkv"
    assert "BluRay" in result.technical_tags
    assert "DDP5.1" in result.technical_tags
    assert "Atmos" in result.technical_tags
    assert not result.review_required


def test_preserves_number_in_mickey_17() -> None:
    result = parse_movie_filename("Mickey.17.2025.1080p.AMZN.WEB-DL.DDP5.1.H264.DUAL-C76.mkv")

    assert result.title == "Mickey 17"
    assert result.year == 2025
    assert result.extension == ".mkv"


def test_parses_a_favorita_release() -> None:
    result = parse_movie_filename("A.Favorita.2019.1080p.BluRay.x264-SPARKS.DUAL-RK.mkv")

    assert result.title == "A Favorita"
    assert result.year == 2019


def test_preserves_channel_metadata_as_one_tag() -> None:
    result = parse_movie_filename("Film.2025.1080p.WEB-DL.DDP5.1.H.264.mkv")

    assert "DDP5.1" in result.technical_tags
    assert "H.264" in result.technical_tags


def test_preserves_numeric_title_before_year() -> None:
    result = parse_movie_filename("1917.2019.1080p.BluRay.x264-GROUP.mkv")

    assert result.title == "1917"
    assert result.year == 2019


def test_parses_without_year_when_technical_boundary_is_clear() -> None:
    result = parse_movie_filename("The.Movie.1080p.WEB-DL.H264.mkv")

    assert result.title == "The Movie"
    assert result.year is None
    assert not result.review_required


def test_marks_ambiguous_years_for_review() -> None:
    result = parse_movie_filename("Movie.2020.2021.1080p.WEB-DL.mkv")

    assert result.title == "Movie"
    assert result.review_required


def test_marks_unbounded_name_for_review() -> None:
    result = parse_movie_filename("Unclear.Movie.Name.mkv")

    assert result.title == "Unclear Movie Name"
    assert result.review_required
