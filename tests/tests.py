import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from .controllers.default import my_view

        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info["project"], "kulturweb")


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from kulturweb import main

        app = main({})
        from webtest import TestApp

        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get_shows("/", status=200)
        self.assertTrue(b"Pyramid" in res.body)