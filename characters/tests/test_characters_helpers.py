import httpx
import pytest

from characters.helpers import check_image_exists, check_images_exist


@pytest.mark.anyio
async def test_check_image_exists_invalid_image():
    """ Test using an invalid_image_url if image exists"""
    invalid_image_url = 'https://invalid.url'
    assert await check_image_exists(invalid_image_url) is False


@pytest.mark.anyio
async def test_check_image_exists_valid_image(mock_valid_images_httpx_client):
    """ Test using valid_image_url (using a mock httpx async client with response status 200)
     if image exists"""
    valid_image_url = 'https://valid.url'
    assert await check_image_exists(valid_image_url) is True

@pytest.mark.anyio
async def test_check_images_exist(mocker):
    """ Test with a valid and an invalid url, using mocker, whether images exist"""
    valid_image_url = 'https://valid.url'
    invalid_image_url = 'https://invalid.url'

    # Define a custom function to determine patch by condition
    async def custom_side_effect(param):
        if param == valid_image_url:
            return True
        else:  # param == invalid_image_url (or something else)
            return False

    # Path the inner function check_image_exists by case (valid and invalid image urls)
    mocker.patch('characters.helpers.check_image_exists', side_effect=custom_side_effect)

    urls = [valid_image_url, invalid_image_url]

    assert await check_images_exist(urls) == [True, False]
