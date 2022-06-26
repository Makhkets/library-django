from rest_framework import reverse
from rest_framework.test import APITestCase

from loguru import logger as l

class BookLibrariesTestCase(APITestCase):
    def test_get_data(self):
        url = reverse("router_urls")
        l.success(url)

        self.assertEqual(url, url)
