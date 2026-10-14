"""Conservative movie release filename parsing."""

import re
from dataclasses import dataclass
from pathlib import PurePath

_YEAR_PATTERN = re.compile(r"^(19\d{2}|20\d{2})$")
_TOKEN_SPLIT_PATTERN = re.compile(r"[._]+")

# Keep this collection easy to extend as new release conventions are found.
TECHNICAL_TAGS = frozenset(
    {
        "2160p",
        "4k",
        "720p",
        "1080p",
        "8bit",
        "10bit",
        "aac",
        "ac3",
        "amzn",
        "atmos",
        "av1",
        "bdrip",
        "bluray",
        "brrip",
        "cr",
        "dd",
        "ddp",
        "dts",
        "dual",
        "dv",
        "eac3",
        "eng",
        "h264",
        "h.264",
        "h265",
        "h.265",
        "hdr",
        "hdr10",
        "hevc",
        "imax",
        "max",
        "multi",
        "nf",
        "opus",
        "remux",
        "sdr",
        "truehd",
        "web-dl",
        "webrip",
        "x264",
        "x265",
    }
)


@dataclass(frozen=True)
class MovieParseResult:
    """The local, non-filesystem result of parsing a movie filename."""

    title: str
    year: int | None
    extension: str
    technical_tags: tuple[str, ...]
    review_required: bool = False


def _clean_token(token: str) -> str:
    return token.strip("[](){}").strip()


def _is_year(token: str) -> bool:
    return _YEAR_PATTERN.fullmatch(_clean_token(token)) is not None


def _is_technical_tag(token: str) -> bool:
    cleaned = _clean_token(token).casefold()
    if cleaned in TECHNICAL_TAGS:
        return True
    if re.fullmatch(r"\d{3,4}p", cleaned) or re.fullmatch(r"\d{1,2}k", cleaned):
        return True
    if re.fullmatch(r"(?:aac|ac3|dd|ddp|dts|eac3|opus|truehd)\d+(?:\.\d+)?", cleaned):
        return True
    # Release groups commonly follow a technical tag after a hyphen.
    prefix = cleaned.split("-", 1)[0]
    return prefix in TECHNICAL_TAGS


def _tokens(stem: str) -> list[str]:
    normalized = _TOKEN_SPLIT_PATTERN.sub(" ", stem)
    raw_tokens = [token for token in normalized.split() if token]
    tokens: list[str] = []
    for token in raw_tokens:
        if (
            tokens
            and token.isdigit()
            and (
                tokens[-1].casefold() in {"h", "dd", "ddp", "dts", "opus", "aac", "ac3", "eac3"}
                or re.fullmatch(r"(?:ddp|dts|opus|aac|ac3|eac3)\d+", tokens[-1].casefold())
            )
        ):
            tokens[-1] = f"{tokens[-1]}.{token}"
        else:
            tokens.append(token)
    return tokens


def parse_movie_filename(filename: str) -> MovieParseResult:
    """Parse a movie release name without reading or changing the filesystem."""
    path = PurePath(filename)
    extension = path.suffix
    tokens = _tokens(path.stem)
    years = [index for index, token in enumerate(tokens) if _is_year(token)]

    year_index = years[0] if years else None
    ambiguous_year = len(years) > 1
    if len(years) > 1 and years[0] == 0:
        # A leading four-digit token can be a numeric title, as in 1917.2019.
        year_index = years[-1]
        ambiguous_year = False
    technical_index = next(
        (index for index, token in enumerate(tokens) if _is_technical_tag(token)),
        None,
    )
    title_end = year_index if year_index is not None else technical_index
    if title_end is None:
        title_end = len(tokens)

    title = " ".join(_clean_token(token) for token in tokens[:title_end]).strip()
    technical_start = year_index if year_index is not None else technical_index
    technical_tags = tuple(
        token
        for index, token in enumerate(tokens)
        if technical_start is not None and index >= technical_start and not _is_year(token)
    )

    review_required = (
        not title or ambiguous_year or (year_index is None and technical_index is None)
    )
    return MovieParseResult(
        title=title,
        year=int(tokens[year_index]) if year_index is not None else None,
        extension=extension,
        technical_tags=technical_tags,
        review_required=review_required,
    )
