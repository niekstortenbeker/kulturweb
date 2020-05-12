from itertools import islice

from kulturweb.viewmodels.data import timespans


def test_get_time_span_options_returns_right_length():
    # WHEN a valid option is already present
    result = timespans.get_time_span_options("heute")
    # THEN six remaining options should be given
    assert len(result) == 6


def test_get_time_span_options_returns_right_length_2():
    # WHEN not a valid option is present (in reality day name for today)
    result = timespans.get_time_span_options("whenever")
    # THEN seven options should be returned
    assert len(result) == 7


def test_get_time_span_options_returns_correct_order():
    # WHEN the option is a specific day
    result = timespans.get_time_span_options("freitag")
    # THEN the first two options should be heute and morgen
    assert list(islice(result, 2)) == ["heute", "morgen"]
