"""Print parsed episode filenames and proposed names without filesystem access."""

import sys

from media_organizer.naming import (
    absolute_episode_filename,
    season_directory,
    series_directory,
    series_episode_filename,
)
from media_organizer.parser import parse_episode_filename


def main() -> None:
    """Parse command-line episode filenames and print proposed names."""
    filenames = sys.argv[1:] or [
        "Jujutsu.Kaisen.S02E04.1080p.BluRay.Opus2.0.x265.DUAL-Anitsu.mkv",
        "Show.S01E01E02.1080p.mkv",
        "Show.S00E01.1080p.mkv",
        "One.Piece.1123.1080p.WEB-DL.mkv",
    ]
    for filename in filenames:
        result = parse_episode_filename(filename)
        if result.review_required:
            proposed = "REVIEW_REQUIRED"
        elif result.absolute_episode is not None:
            proposed = f"{series_directory(result.title)}/{absolute_episode_filename(result.title, result.absolute_episode, result.extension)}"
        else:
            proposed = (
                f"{series_directory(result.title)}/{season_directory(result.season or 0)}/"
                f"{series_episode_filename(result.title, result.season or 0, result.episodes, result.extension)}"
            )
        print(f"{filename} -> {result} -> {proposed}")


if __name__ == "__main__":
    main()
