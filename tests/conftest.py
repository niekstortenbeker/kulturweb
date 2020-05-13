import pytest


@pytest.fixture(scope="session")
def test_app():
    from kulturweb import main

    app = main({})
    from webtest import TestApp

    return TestApp(app)
