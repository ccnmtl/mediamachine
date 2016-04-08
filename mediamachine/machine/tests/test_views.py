from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from mediamachine.machine.models import Video


class SimpleViewTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_index(self):
        result = self.c.get("/")
        self.assertEqual(result.status_code, 302)

    def test_smoketest(self):
        self.c.get("/smoketest/")


class LoggedInTest(TestCase):
    def setUp(self):
        self.u = User.objects.create(username="test")
        self.u.set_password("test")
        self.u.save()
        self.c = Client()
        self.c.login(username="test", password="test")

    def test_index(self):
        result = self.c.get("/")
        self.assertEqual(result.status_code, 200)

    def test_video_index(self):
        result = self.c.get("/video/")
        self.assertEqual(result.status_code, 200)

    def test_theme_index(self):
        result = self.c.get("/theme/")
        self.assertEqual(result.status_code, 200)

    def test_keyword_index(self):
        result = self.c.get("/keyword/")
        self.assertEqual(result.status_code, 200)

    def test_video_detail(self):
        v = Video.objects.create()
        result = self.c.get(v.get_absolute_url())
        self.assertEqual(result.status_code, 200)
