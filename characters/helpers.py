import asyncio

import httpx


async def check_image_exists(url: str) -> bool:
    """
    Check if the image from the specific url exists
    :param url: the image url
    :return: True if it exists False otherwise
    """
    async with httpx.AsyncClient() as client:
        try:
            response = await client.head(url, timeout=5)
            return response.status_code == 200
        except httpx.RequestError:
            return False


async def check_images_exist(urls: list[str]) -> list[bool]:
    """
    Check if the images related to the urls
    passed as parameter exist
    :param urls: a list containing the images' urls
    :return: a list of booleans showing whether each image exists or not
    """
    tasks = [check_image_exists(url) for url in urls]
    return await asyncio.gather(*tasks)