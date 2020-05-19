import pyramid.testing
import pytest
from pyramid.httpexceptions import HTTPNotFound


def test_home(mock_get_shows, filter_dummy_request):
    # GIVEN a fake return from get_shows and a dummy request
    from kulturweb.views import default

    # WHEN home view method is called
    # noinspection PyTypeChecker
    model = default.home(filter_dummy_request)
    # THEN shows should be returned
    assert model
    assert model["shows"][1].title == "adventures in the dark"


def test_filter(mock_get_shows, filter_dummy_request):
    # GIVEN a fake return from get_shows and a dummy request with the right keys
    # WHEN filter view method is called
    from kulturweb.views.default import filter_shows

    # noinspection PyTypeChecker
    model = filter_shows(filter_dummy_request)
    # THEN shows should be returned
    assert model
    assert model["shows"][1].title == "adventures in the dark"


def test_filter_404(mock_get_shows):
    # GIVEN a fake return from get_shows and a dummy request with a false location str
    request = pyramid.testing.DummyRequest()
    request.matchdict = {
        "dubbed": "ja",
        "category": "alle",
        "time_span": "morgen",
        "location": "galaxy",
    }
    # WHEN filter view method is called
    # THEN shows should be returned
    from kulturweb.views.default import filter_shows

    with pytest.raises(HTTPNotFound):
        # noinspection PyTypeChecker
        filter_shows(request)


def test_impressum():
    # GIVEN dummy request
    request = pyramid.testing.DummyRequest()
    # WHEN impressum view method is called
    from kulturweb.views.meta import impressum

    # noinspection PyTypeChecker
    model = impressum(request)
    # THEN an empty dict should be returned
    assert not model


def test_about():
    # GIVEN dummy request
    request = pyramid.testing.DummyRequest()
    # WHEN about view method is called
    from kulturweb.views.meta import about

    # noinspection PyTypeChecker
    model = about(request)
    # THEN an empty dict should be returned
    assert not model


def test_not_found():
    # GIVEN dummy request
    request = pyramid.testing.DummyRequest()
    # WHEN 404 view method is called
    from kulturweb.views.notfound import notfound_view

    # noinspection PyTypeChecker
    model = notfound_view(request)
    # THEN an empty dict should be returned
    assert not model
