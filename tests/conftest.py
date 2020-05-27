import arrow
import pytest
from kultur.data.show import Show
from kulturweb.viewmodels.data import shows
from pyramid.testing import DummyRequest


@pytest.fixture(scope="session")
def test_app():
    from kulturweb import main

    app = main({})
    from webtest import TestApp

    return TestApp(app)


@pytest.fixture()
def mock_get_shows(mocker):
    show = Show()
    show.title = "adventures in the dark"
    show.description = "Amazing adventures in the dark, what a spectacle"
    show.date_time = arrow.get("2020-05-18 20:30").replace(tzinfo="Europe/Berlin")
    show.day = "MO 18.05"  # not automatically generated because not added to db
    show.location = "City 46"
    show.category = "cinema"
    show.url_info = "https://www.nothing.de"

    mocker.patch.object(shows, "get_shows", return_value=[show])

    yield


@pytest.fixture(scope="session")
def filter_dummy_request():
    request = DummyRequest()
    request.matchdict = {
        "dubbed": "ja",
        "category": "alle",
        "time_span": "morgen",
        "location": "schauburg",
    }
    request.registry.settings = {"kulturweb.app_url": "http://localhost:6543/"}
    return request
