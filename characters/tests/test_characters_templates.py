import pytest

from django.test import TestCase
from django.urls import reverse

from characters.tests.conftest import fake_futurama_data


@pytest.mark.django_db
@pytest.mark.usefixtures("mock_synced_httpx_client")
class CharacterTemplateTest(TestCase):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, fake_futurama_data, request):
        self.data = fake_futurama_data
        # self.mock_valid_images_httpx_client = mock_valid_images_httpx_client

    def test_characters_list_template_content(self):
        response = self.client.get(reverse('characters_list'))
        self.assertContains(response, '<h2 class="section-heading text-uppercase">Futurama Hall of Fame</h2>')

    def test_characters_list_data_check_in_template(self):
        # Make the GET request to the character list
        resp = self.client.get(reverse('characters_list'))

        # List of expected full names, considering only first and last names
        expected_names = [
            " ".join([char['name']['first'], char['name']['last']])
            for char in self.data]

        # Use all() with a comprehension to assert all names are in the response content
        assert all(name in resp.content.decode('utf-8') for name in expected_names), \
            "Not all expected names found in the response content"
