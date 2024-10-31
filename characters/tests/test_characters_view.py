import pytest

from django.test import TestCase
from django.urls import reverse

@pytest.mark.usefixtures("mock_synced_httpx_client")
class TestCharactersListView(TestCase):
    def test_characters_list_view(self):
        response = self.client.get(reverse('characters_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'characters/characters_list.html')
