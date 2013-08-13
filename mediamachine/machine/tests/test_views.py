from django.test import TestCase
from django.test.client import Client


class SimpleViewTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index(self):
        result = self.c.get("/")
        self.assertEqual(result.status_code, 302)

    def test_smoketest(self):
        result = self.c.get("/smoketest/")
        self.assertEqual(result.status_code, 200)
