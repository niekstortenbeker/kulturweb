from typing import List, Tuple, Union

import arrow
import kultur
from kultur.data.show import Show

Arrow = arrow.Arrow


def get_shows(time_span: str, category: str, dubbed: str) -> List[Union[Show, str]]:
    start, stop = _start_and_stop_times(time_span)
    category = _translate_category(category)
    dubbed = _translate_dubbed(dubbed)
    shows = kultur.get_shows(start, stop, category, dubbed)
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


def _translate_dubbed(dubbed: str) -> bool:
    translate = {"ja": True, "nein": False}

    if type(dubbed) != str:
        raise TypeError("only str accepted")
    if dubbed not in translate.keys():
        raise ValueError(f'"Only {translate.keys()} accepted')

    return translate[dubbed]


def _translate_category(category: str) -> str:
    categories = {"alle": "all", "kino": "cinema", "buehne": "stage", "musik": "music"}

    if type(category) != str:
        raise TypeError("Only str accepted")
    if category not in categories.keys():
        raise ValueError(f'"Only these categories accepted: {list(categories.keys())}')

    return categories[category]


def _start_and_stop_times(time_span: str) -> Tuple[Arrow, Arrow]:
    times = {
        "heute": (arrow.now("Europe/Berlin"), _arrow_shift_days_from_today(1)),
        "morgen": (_arrow_shift_days_from_today(1), _arrow_shift_days_from_today(2),),
        "uebermorgen": (
            _arrow_shift_days_from_today(2),
            _arrow_shift_days_from_today(3),
        ),
        "woche": (arrow.now("Europe/Berlin"), _arrow_shift_days_from_today(7)),
    }
    if type(time_span) != str:
        raise TypeError("Only accepts strings")
    if time_span not in times.keys():
        raise ValueError(f'"Only accepts these categories: {list(times.keys())}')

    return times[time_span]


def _arrow_shift_days_from_today(days: int) -> Arrow:
    return (
        arrow.now("Europe/Berlin")
        .shift(days=days)
        .replace(hour=0, minute=0, second=0, microsecond=0)
    )
