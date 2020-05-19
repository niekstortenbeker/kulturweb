import arrow
import pytest
from kulturweb.viewmodels.data import shows


def test_translate_timespan_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        shows._translate_time_span("this ball")


def test_translate_timespan_returns_heute():
    # noinspection PyProtectedMember
    start, stop = shows._translate_time_span("heute")
    days = (stop - start).days
    # days rounded (down) should be 0
    assert days == 0


def test_translate_timespan_returns_today():
    # noinspection PyProtectedMember
    today = arrow.now("Europe/Berlin").format("dddd", locale="de").lower()
    start, stop = shows._translate_time_span(today)
    days = (stop - start).days
    # days rounded (down) should be 0
    assert days == 0
