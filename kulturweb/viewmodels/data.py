from typing import List

import arrow
from kulturweb.data.dbsession import DbSession, UninitializedDatabaseError
from kulturweb.data.show import Show

Arrow = arrow.Arrow


def get_shows(time_span, location, category, dubbed):
    shows = ShowsGetter(time_span, location, category, dubbed)
    return shows.get()


class ShowsGetter:
    def __init__(self, time_span, location, category, dubbed):
        if time_span not in ["heute", "morgen", "uebermorgen", "woche"]:
            raise ValueError("not an accepted time span")
        if category not in ["alle", "kino", "buehne", "musik"]:
            raise ValueError("not a valid category")
        if dubbed not in ["ja", "nein"]:
            raise ValueError('only "ja" or "nein" is accepted')
        if not DbSession.factory:
            raise UninitializedDatabaseError

        self.time_span = time_span
        self.location = location
        self.category = category
        self.dubbed = True if dubbed == "ja" else False
        self._session = DbSession.factory()

    def get(self):
        if self.category == "alle":
            pass
        self.query_program_category()
        # TODO
        return None

    def query_program_category(self) -> List[Show]:
        return (
            self._session.query(Show)
            .filter_by(category=self.category)
            .filter_by(dubbed=self.dubbed)
            .filter(Show.date_time.between(*self._start_and_stop()))
            .order_by(Show.date_time)
            .all()
        )

    def _start_and_stop(self) -> List[Arrow]:
        times = {
            "heute": [arrow.now("Europe/Berlin"), _arrow_shift_days_from_today(1)],
            "morgen": [
                _arrow_shift_days_from_today(1),
                _arrow_shift_days_from_today(2),
            ],
            "uebermorgen": [
                _arrow_shift_days_from_today(2),
                _arrow_shift_days_from_today(3),
            ],
            "woche": [arrow.now("Europe/Berlin"), _arrow_shift_days_from_today(7)],
        }
        return times[self.time_span]


def _arrow_shift_days_from_today(days: int) -> Arrow:
    return (
        arrow.now("Europe/Berlin")
        .shift(days=days)
        .replace(hour=0, minute=0, second=0, microsecond=0)
    )
