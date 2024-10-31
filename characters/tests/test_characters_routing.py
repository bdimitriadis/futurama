from django.test import TestCase
from django.urls import reverse, resolve
from characters.views import characters_list

class URLRoutingTest(TestCase):
    def test_character_list_url_resolves(self):
        url = reverse('characters_list')
        self.assertEqual(resolve(url).func, characters_list)
