import arrow
import pytest
from kulturweb.viewmodels.data import shows


def test_translate_dubbed_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        shows._translate_dubbed("yeah")


def test_translate_dubbed_raises_type_error():
    with pytest.raises(TypeError):
        # noinspection PyProtectedMember,PyTypeChecker
        shows._translate_dubbed(True)


def translate_dubbed_returns_true():
    # noinspection PyProtectedMember
    result = shows._translate_dubbed("ja")
    expectation = True
    assert result == expectation


def test_translate_category_raises_type_error():
    with pytest.raises(TypeError):
        # noinspection PyProtectedMember,PyTypeChecker
        shows._translate_category(True)


def test_translate_category_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        shows._translate_category("tree")


def test_translate_category_returns_music():
    # noinspection PyProtectedMember
    result = shows._translate_category("musik")
    expectation = "music"
    assert result == expectation


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
