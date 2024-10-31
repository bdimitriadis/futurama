import os

import django
import pytest

from characters.tests.helpers import FuturamaProvider

from unittest.mock import AsyncMock, Mock

from django.conf import settings
from faker import Faker
from httpx import Request, Response


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "futurama.settings")

# If Django hasn’t been set up, do so now
if not settings.configured:
    django.setup()


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture()
def mock_valid_images_httpx_client(mocker):
    """ Fixture for mocked async client to be used for the images existence check"""
    mocked_client = mocker.patch("characters.helpers.httpx.AsyncClient")

    mocked_async_client = Mock()
    response = Response(status_code=200, request=Request("HEAD", "//"))
    mocked_async_client.head = AsyncMock(return_value=response)
    mocked_client.return_value.__aenter__.return_value = mocked_async_client

    return mocked_async_client


@pytest.fixture
def fake_futurama_data():
    """ Fixture for creating fake futurama characters"""

    # Register the provider with Faker
    fake = Faker()
    fake.add_provider(FuturamaProvider)

    def split_full_name(full_name):
        # Split the name into parts
        name_parts = full_name.split()

        # Initialize the dictionary with default values
        name_dict = {
            'first': "",
            'middle': "",
            'last': ""
        }

        # Determine the number of name parts
        if len(name_parts) == 0:
            # No name provided
            return name_dict
        elif len(name_parts) == 1:
            # Only first name is provided
            name_dict['first'] = name_parts[0]
        elif len(name_parts) == 2:
            # First name and last name are provided
            name_dict['first'] = name_parts[0]
            name_dict['last'] = name_parts[1]
        else:
            # First name, possible middle name(s), and last name
            name_dict['first'] = name_parts[0]
            name_dict['last'] = name_parts[-1]
            name_dict['middle'] = ''.join(name_parts[1:-1])  # Join middle parts into a string

        return name_dict

    # Generate random characters
    return [{
        "name": split_full_name(fake.full_name()),
        "gender": fake.gender(),
        "species": fake.species(),
        "occupation": fake.occupation(),
        "sayings": fake.sayings(),
        "images": {"main": fake.image_url()}
    } for _ in range(settings.PROFILES_PER_PAGE)]


@pytest.fixture()
def mock_synced_httpx_client(mocker, fake_futurama_data):
    # Mock the Client in the view
    mocked_client = mocker.patch('characters.views.httpx.get')

    # Create a mock response object with the fake data
    request = Request("GET", "//")
    mock_response = Response(200, request=request, json=fake_futurama_data)

    # Set the return value of the get method to our mock response
    mocked_client.return_value = mock_response
