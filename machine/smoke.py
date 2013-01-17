from smoketest import SmokeTest
from models import Resource


class DBConnectivity(SmokeTest):
    def test_retrieve(self):
        cnt = Resource.objects.all().count()
        self.assertTrue(cnt > 0)
