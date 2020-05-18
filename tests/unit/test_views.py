import pyramid.testing
import pytest
from pyramid.httpexceptions import HTTPNotFound


def test_home(shows_list, mocker):
    # GIVEN a fake return from get_shows and a dummy request
    from kulturweb.viewmodels.data import shows

    request = pyramid.testing.DummyRequest()
    mocker.patch.object(shows, "get_shows", return_value=shows_list)
    # WHEN home view method is called
    from kulturweb.views.default import home

    # noinspection PyTypeChecker
    model = home(request)
    # THEN shows should be returned
    assert model
    assert model[1].title == "adventures in the dark"


def test_filter(shows_list, mocker):
    # GIVEN a fake return from get_shows and a dummy request with the right keys
    from kulturweb.viewmodels.data import shows

    request = pyramid.testing.DummyRequest()
    request.matchdict = {
        "dubbed": "ja",
        "category": "alle",
        "time_span": "morgen",
        "location": "schauburg",
    }
    mocker.patch.object(shows, "get_shows", return_value=shows_list)
    # WHEN filter view method is called
    from kulturweb.views.default import filter_shows

    # noinspection PyTypeChecker
    model = filter_shows(request)
    # THEN shows should be returned
    assert model
    assert model[1].title == "adventures in the dark"


def test_filter_404(shows_list, mocker):
    # GIVEN a fake return from get_shows and a dummy request with a false location str
    from kulturweb.viewmodels.data import shows

    request = pyramid.testing.DummyRequest()
    request.matchdict = {
        "dubbed": "ja",
        "category": "alle",
        "time_span": "morgen",
        "location": "galaxy",
    }
    mocker.patch.object(shows, "get_shows", return_value=shows_list)
    # WHEN filter view method is called
    from kulturweb.views.default import filter_shows

    # THEN shows should be returned
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
