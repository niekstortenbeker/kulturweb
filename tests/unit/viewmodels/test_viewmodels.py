import pytest
from kulturweb.viewmodels.viewmodel_default import FilterViewModel, HomeViewModel
from pyramid.testing import DummyRequest


def test_filterviewmodel_no_error(filter_dummy_request):
    # GIVEN a dummy request with the right keys
    # WHEN FilterViewModel is instantiated and validated
    # noinspection PyTypeChecker
    vm = FilterViewModel(filter_dummy_request)
    vm.validate()
    # THEN there should be no error
    assert not vm.error


request_dicts = [
    {
        "dubbed": "True",
        "category": "alle",
        "time_span": "morgen",
        "location": "schauburg",
    },
    {
        "dubbed": "ja",
        "category": "blub",
        "time_span": "morgen",
        "location": "schauburg",
    },
    {
        "dubbed": "ja",
        "category": "alle",
        "time_span": "in five weeks",
        "location": "schauburg",
    },
    {"dubbed": "ja", "category": "alle", "time_span": "morgen", "location": "galaxy"},
]
request_dicts_ids = ["dubbed", "category", "time_span", "location"]


@pytest.mark.parametrize("request_dict", request_dicts, ids=request_dicts_ids)
def test_filterviewmodel_has_error(request_dict):
    # GIVEN a dummy request with a wrong key
    request = DummyRequest()
    request.matchdict = request_dict
    # WHEN FilterViewModel is instantiated, and validated
    # noinspection PyTypeChecker
    vm = FilterViewModel(request)
    vm.validate()
    # THEN there should be an error
    assert vm.error == "not a valid url"


def test_filterviewmodel_has_shows(mock_get_shows, filter_dummy_request):
    # GIVEN a dummy request with the right keys and get_shows is mocked
    # WHEN FilterViewModel is instantiated, validated, and set_shows()
    # noinspection PyTypeChecker
    vm = FilterViewModel(filter_dummy_request)
    vm.validate()
    vm.set_shows()
    # THEN there should be shows
    assert vm.shows
    assert vm.time_span


def test_filterviewmodel_has_timespan_options(mock_get_shows, filter_dummy_request):
    # GIVEN a dummy request with the right keys and get_shows is mocked
    # WHEN FilterViewModel is instantiated, validated, and set_shows()
    # noinspection PyTypeChecker
    vm = FilterViewModel(filter_dummy_request)
    vm.validate()
    vm.set_shows()
    # THEN there should be shows
    assert vm.time_span_options


def test_homeviewmodel_has_shows(mock_get_shows):
    # GIVEN a dummy request and get_shows is mocked
    request = DummyRequest()
    # WHEN HomeViewModel is instantiated
    # noinspection PyTypeChecker
    vm = HomeViewModel(request)
    # THEN there should be shows
    assert vm.shows


def test_homeviewmodel_has_timespan_options(mock_get_shows):
    # GIVEN a dummy request and get_shows is mocked
    request = DummyRequest()
    # WHEN HomeViewModel is instantiated
    # noinspection PyTypeChecker
    vm = HomeViewModel(request)
    # THEN there should  time span options
    assert vm.time_span_options
