"""Print representative naming results without touching the filesystem."""

from media_organizer.naming import (
    absolute_episode_filename,
    movie_filename,
    series_episode_filename,
    subtitle_filename,
)


def main() -> None:
    """Print representative Alfa naming examples."""
    print(movie_filename("John Wick Chapter 4", ".mkv"))
    print(series_episode_filename("Jujutsu Kaisen", 2, [4], ".mkv"))
    print(series_episode_filename("Show", 1, [1, 2], ".mkv"))
    print(series_episode_filename("Show", 0, [1], ".mkv"))
    print(absolute_episode_filename("One Piece", 1123, ".mkv"))
    print(subtitle_filename("A Favorita", ".srt", "pt-BR", ["forced"]))


if __name__ == "__main__":
    main()
