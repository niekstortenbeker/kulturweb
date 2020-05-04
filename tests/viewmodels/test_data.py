import pytest
from kulturweb.viewmodels import data


def test_translate_dubbed_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        data._translate_dubbed("yeah")


def test_translate_dubbed_raises_type_error():
    with pytest.raises(TypeError):
        # noinspection PyProtectedMember,PyTypeChecker
        data._translate_dubbed(True)


def translate_dubbed_returns_true():
    # noinspection PyProtectedMember
    result = data._translate_dubbed("ja")
    expectation = True
    assert result == expectation


def test_translate_category_raises_type_error():
    with pytest.raises(TypeError):
        # noinspection PyProtectedMember,PyTypeChecker
        data._translate_category(True)


def test_translate_category_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        data._translate_category("tree")


def test_translate_category_returns_music():
    # noinspection PyProtectedMember
    result = data._translate_category("musik")
    expectation = "music"
    assert result == expectation


def test_start_raises_value_error():
    with pytest.raises(ValueError):
        # noinspection PyProtectedMember
        data._start_and_stop_times("this ball")


def test_start_returns_week():
    # noinspection PyProtectedMember
    start, stop = data._start_and_stop_times("woche")
    days = (stop - start).days
    # a week (rounded down) should have 6 or 7 days
    assert 5 < days < 8
