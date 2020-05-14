from typing import Dict, List, Tuple, Union

import arrow
import kultur
from kultur.data.show import Show

Arrow = arrow.Arrow

valid_dubbed = {"ja": True, "nein": False}
valid_categories = {
    "alle": "all",
    "kino": "cinema",
    "buehne": "stage",
    "musik": "music",
}
valid_locations: Dict = kultur.get_location_names()
valid_time_spans = [
    "heute",
    "morgen",
    "montag",
    "dienstag",
    "mittwoch",
    "donnerstag",
    "freitag",
    "samstag",
    "sonntag",
]


def get_shows(
    time_span: str, category: str, dubbed: str, location: str
) -> List[Union[Show, str]]:
    start, stop = _translate_time_span(time_span)
    category = valid_categories[category]
    location = valid_locations[location]
    dubbed = valid_dubbed[dubbed]
    shows = kultur.get_shows(start, stop, category, dubbed, location)
    return _insert_days(shows)


def _insert_days(shows: List[Show]) -> List[Union[Show, str]]:
    new_shows = []
    day = ""
    for show in shows:
        if show.day != day:
            day = show.day
            new_shows.append(day)
            new_shows.append(show)
        else:
            new_shows.append(show)
    return new_shows


def _translate_time_span(time_span: str) -> Tuple[Arrow, Arrow]:
    if time_span == "heute":
        return arrow.now("Europe/Berlin"), _normalize_shift_arrow(1)
    elif time_span == "morgen":
        return _normalize_shift_arrow(1), _normalize_shift_arrow(2)

    days_shift = _count_days_shift(time_span)
    if days_shift == 0:
        return arrow.now("Europe/Berlin"), _normalize_shift_arrow(1)
    else:
        return (
            _normalize_shift_arrow(days_shift),
            _normalize_shift_arrow(days_shift + 1),
        )


def _count_days_shift(time_span: str) -> int:
    days = [
        "montag",
        "dienstag",
        "mittwoch",
        "donnerstag",
        "freitag",
        "samstag",
        "sonntag",
        "montag",
        "dienstag",
        "mittwoch",
        "donnerstag",
        "freitag",
        "samstag",
        "sonntag",
    ]
    today = arrow.now("Europe/Berlin").format("dddd", locale="de").lower()
    idx_today = days.index(today)
    return days.index(time_span, idx_today) - idx_today


def _normalize_shift_arrow(days_shift: int) -> Arrow:
    return (
        arrow.now("Europe/Berlin")
        .shift(days=days_shift)
        .replace(hour=0, minute=0, second=0, microsecond=0)
    )
