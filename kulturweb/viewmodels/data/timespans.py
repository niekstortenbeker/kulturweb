from typing import Dict

import arrow
from kulturweb.viewmodels.data.shows import Arrow


def get_time_span_options(current_time_span: str) -> Dict:
    """
    returns a dict that maps url_names to title_names for time span options
    it doesn't include the current time span option
    """
    now = arrow.now("Europe/Berlin")
    days = {
        "heute": "Heute",
        "morgen": "Morgen",
    }

    for i in range(2, 7):
        day = now.shift(days=+i)
        days[_url_name(day)] = _title_name(day)

    if current_time_span in days:
        days.pop(current_time_span)

    return days


def _url_name(date_time: Arrow):
    return date_time.format("dddd", locale="de").lower()


def _title_name(date_time: Arrow):
    return date_time.format("dddd", locale="de")
