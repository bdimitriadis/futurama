import httpx
import logging

from django.conf import settings
from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.templatetags.static import static

from characters.helpers import check_images_exist


logger = logging.getLogger('characters')


def get_cached_response(url, params=None, cache_timeout=300):
    """Fetches and caches an httpx response for a given URL."""

    # Create a unique cache key based on the URL and parameters
    cache_key = f"httpx_cache:{url}:{str(params)}"

    # Try to retrieve cached data
    cached_response = cache.get(cache_key)
    if cached_response:
        return cached_response

    # If not cached, make the HTTP request
    try:
        response = httpx.get(url, params=params)
        response.raise_for_status()

        # Cache the response JSON content
        cache.set(cache_key, response.json(), timeout=cache_timeout)
        return response.json()

    except httpx.HTTPError as e:
        # Handle the exception as needed
        logger.error(f"An error occurred: {e}")
        return None


async def characters_list(request):
    """
    Controller to retrieve each character's details from the REST API
    and format/display them appropriately for the client view.
    :param request: request
    :return: the characters list view
    """

    # Call the function to get cached data or make the request and fetch data from external API
    try:
        characters = get_cached_response(settings.FUTURAMA_API_URL, cache_timeout=300)

        image_urls = []

        # Process and paginate characters
        for character in characters:
            character['full_name'] = f"{character['name']['first']} {character['name']['last']}"
            character['image_url'] = f"{character['images'].get('main', '')}"
            image_urls.append(character['image_url'])

        # Check if images exist for every character and do that asynchronously
        images_mask = await check_images_exist(image_urls)

        for indx, exists_flag in enumerate(images_mask):
            # If image does not exist use a default not-available image
            if exists_flag is False:
               characters[indx]['image_url'] = static('characters/img/picture-not-available.jpg')

        # Paginate results - display a specific number of profiles per page
        paginator = Paginator(characters, settings.PROFILES_PER_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
    except Exception as e:
        logger.error("Unhandled exception: %s", e)
        return render(request, "characters/errors/500.html", status=500)



    logger.debug("Rendering characters_list.html template")

    return render(request, 'characters/characters_list.html', {'page_obj': page_obj})

def error_404(request, exception):
    """ Custom 404 error page """
    return render(request, "characters/errors/404.html", status=404)

def error_500(request):
    return render(request, "500.html", status=500)
