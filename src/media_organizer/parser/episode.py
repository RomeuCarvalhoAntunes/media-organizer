"""Conservative parsing for series and anime episode filenames."""

import re
from dataclasses import dataclass
from pathlib import PurePath

from media_organizer.parser.movie import _is_technical_tag, _is_year, _tokens

_EPISODE_PATTERN = re.compile(
    r"(?i)(?:^|[._ -])S(?P<season>\d{1,2})E(?P<episodes>\d{1,3}(?:E\d{1,3})*)"
)
_ABSOLUTE_ANIME_SIGNALS = (
    "bleach",
    "boruto",
    "dragon ball",
    "naruto",
    "one piece",
    "pokemon",
)


@dataclass(frozen=True)
class EpisodeParseResult:
    """The local, non-filesystem result of parsing an episode filename."""

    title: str
    extension: str
    season: int | None = None
    episodes: tuple[int, ...] = ()
    absolute_episode: int | None = None
    review_required: bool = False


def _title_from_prefix(prefix: str) -> str:
    tokens = [token for token in re.sub(r"[._]+", " ", prefix).split() if token]
    return " ".join(token.strip("[](){}").strip() for token in tokens).strip()


def _parse_absolute_episode(stem: str, extension: str) -> EpisodeParseResult:
    tokens = _tokens(stem)
    technical_index = next(
        (index for index, token in enumerate(tokens) if _is_technical_tag(token)),
        len(tokens),
    )
    candidates = [
        (index, int(token))
        for index, token in enumerate(tokens[:technical_index])
        if token.isdigit() and int(token) >= 1000 and not _is_year(token)
    ]
    if not candidates:
        return EpisodeParseResult(" ".join(tokens), extension, review_required=True)

    index, absolute_episode = candidates[-1]
    title = " ".join(tokens[:index]).strip()
    strong_signal = any(signal in title.casefold() for signal in _ABSOLUTE_ANIME_SIGNALS)
    return EpisodeParseResult(
        title=title,
        extension=extension,
        absolute_episode=absolute_episode,
        review_required=not title or not strong_signal or len(candidates) > 1,
    )


def parse_episode_filename(filename: str) -> EpisodeParseResult:
    """Parse a series, special, or absolute-anime filename read-only."""
    path = PurePath(filename)
    match = _EPISODE_PATTERN.search(path.stem)
    if match:
        episode_values = tuple(int(value) for value in re.findall(r"\d+", match.group("episodes")))
        title = _title_from_prefix(path.stem[: match.start()])
        return EpisodeParseResult(
            title=title,
            extension=path.suffix,
            season=int(match.group("season")),
            episodes=episode_values,
            review_required=not title or not episode_values,
        )
    return _parse_absolute_episode(path.stem, path.suffix)
