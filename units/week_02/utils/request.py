import json, os
import urllib.error, urllib.request, urllib.parse

from .read_json import read_json
from .write_json import write_json

def redact_api_key(url: str) -> str:
    """Redact the Steam API key from the given string if it's present"""
    return url.replace(os.environ['STEAM_API_KEY'], '__REDACTED_API_KEY__')

def generate_request_cache_file_path(url: str) -> str:
    """Generate a safe file path for caching the response of a request to the given URL"""
    # URL-encode the URL to make it safe for use as a filename
    processed_url = urllib.parse.quote(url)

    # Replace any slashes with underscores to avoid subdirectory issues
    processed_url = processed_url.replace('/', '_')

    # Redact the API key if it's present in the URL
    processed_url = redact_api_key(processed_url)

    # Return the full relative path
    return f'request_cache/{processed_url}.json'

def request(url: str, squelch:bool=False, throw_error:bool=False) -> dict|None:
    """
    Perform a cached HTTP GET request to the specified URL and return the JSON response as a
    dictionary. Will automatically save the response to a cache file and use the cached version
    if it exists

    Args:
        url (str): The URL to send the GET request to
        squelch (bool): If True, will not print messages about using cached data
        throw_error (bool): If True, will raise an exception on HTTP errors instead of returning None

    Returns:
        dict|None: The JSON body response from the URL as a dictionary or None if there was an error
    """
    # First check the cache
    cache_path = generate_request_cache_file_path(url)
    cached_data = read_json(cache_path)
    if cached_data:
        # We found some cached data! (It's not None)
        if not squelch:
            print(f"    Using cached data for request to {redact_api_key(url)}")
        return cached_data

    json_content = None
    try:
        with urllib.request.urlopen(url) as response:
            # Read and decode the response
            body_content = response.read().decode('utf-8')
            json_content = json.loads(body_content)
    except urllib.error.URLError as e:
        if throw_error:
            raise e
        print(f"Error accessing URL: {e.reason}")
    except Exception as e:
        if throw_error:
            raise e
        print(f"An unexpected error occurred: {e}")

    # Write the response to the cache if it exists
    if json_content: write_json(cache_path, json_content)
    return json_content
