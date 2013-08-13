from django.test import TestCase
from mediamachine.machine.models import Resource
from mediamachine.machine.models import Theme
from mediamachine.machine.models import Keyword
from mediamachine.machine.models import Video


class ResourceTest(TestCase):
    def test_unicode(self):
        r = Resource.objects.create()
        self.assertEqual(str(r), "")

    def test_get_absolute_url(self):
        r = Resource.objects.create()
        self.assertEqual(r.get_absolute_url(), "/resource/%d/" % r.id)


class ThemeTest(TestCase):
    def test_unicode(self):
        r = Theme.objects.create()
        self.assertEqual(str(r), "")

    def test_get_absolute_url(self):
        r = Theme.objects.create()
        self.assertEqual(r.get_absolute_url(), "/theme/%d/" % r.id)


class KeywordTest(TestCase):
    def test_unicode(self):
        r = Keyword.objects.create()
        self.assertEqual(str(r), "")

    def test_get_absolute_url(self):
        r = Keyword.objects.create()
        self.assertEqual(r.get_absolute_url(), "/keyword/%d/" % r.id)


class VideoTest(TestCase):
    def test_unicode(self):
        r = Video.objects.create()
        self.assertEqual(str(r), "")

        r.scene = "foo"
        self.assertEqual(str(r), ": foo")

    def test_get_absolute_url(self):
        r = Video.objects.create()
        self.assertEqual(r.get_absolute_url(), "/video/%d/" % r.id)

    def test_images(self):
        r = Video.objects.create(sequence_count=2)
        images = list(r.images())
        self.assertEqual(
            images,
            [u'http://www.columbia.edu/itc/tc/cstudies/imagesequence/1.jpg'])
