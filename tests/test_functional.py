import kultur
import pytest
from webtest import response as r


def urls():
    categories = ["kino", "buehne", "musik"]
    locations = list(kultur.get_location_names().keys())
    timespans = [
        "heute",
        "morgen",
        "montag",
        "dienstag",
        "mittwoch",
        "donnerstag",
        "freitag",
        "samstag",
        "sonntag",
    ]
    dubbed = ["ja", "nein"]
    url_list = []
    id_list = []
    for category in categories:
        for location in locations:
            for timespan in timespans:
                for dubbed_option in dubbed:
                    url_list.append(
                        f"/{category}/{location}/wann={timespan}+synchronisierter={dubbed_option}#settings"
                    )
                    id_list.append(
                        f"{category}, {location}, {timespan}, {dubbed_option}"
                    )
    return url_list, id_list


all_urls, all_ids = urls()


def test_home(test_app):
    # GIVEN a webtest test app
    # WHEN the home page is requested
    response: r.TestResponse = test_app.get("/", status=200)
    # THEN the tag show-list should be present
    assert b"show-list" in response.body


@pytest.mark.parametrize("url", all_urls, ids=all_ids)
def test_all_urls(test_app, url):
    # GIVEN a webtest test app
    # WHEN any of the filter options pages are requested
    response: r.TestResponse = test_app.get(url, status=200)
    # THEN the tag show-list should be present
    assert b"show-list" in response.body


def test_tomorrow_has_shows(test_app):
    # GIVEN a webtest test app
    # WHEN tomorrow's program is requested
    url = f"/alle/alle/wann=morgen+synchronisierter=ja#settings"
    response: r.TestResponse = test_app.get(url, status=200)
    # THEN there should be a show with a title ('class="title"')
    assert b'class="title"' in response.body
