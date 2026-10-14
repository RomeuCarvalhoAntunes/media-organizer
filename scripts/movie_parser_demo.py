"""Print parsed movie filenames without touching the filesystem."""

import sys

from media_organizer.parser import parse_movie_filename


def main() -> None:
    """Parse command-line filenames or a representative default example."""
    filenames = sys.argv[1:] or [
        "John.Wick.Chapter.4.2023.BluRay.1080p.DDP5.1.Atmos.x264-MTeam.DUAL-C76.mkv",
        "Mickey.17.2025.1080p.AMZN.WEB-DL.DDP5.1.H264.DUAL-C76.mkv",
    ]
    for filename in filenames:
        print(f"{filename} -> {parse_movie_filename(filename)}")


if __name__ == "__main__":
    main()
