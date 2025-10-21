from typing import Callable

from .request import request

def get_game_data(app_id:str, squelch:bool=False, squelch_request:bool=False, throw_http_error:bool=False) -> None|dict:
    """
    Retrieves detailed information about a game from the Steam Store API using its app ID

    Args:
        app_id (str): The Steam app ID of the game to retrieve details for
        squelch (bool): If True, will not print messages about the retrieval process
        squelch_request (bool): If True, will not print messages from the request function
        throw_http_error (bool): If True, will raise an exception on HTTP errors instead of returning None
    Returns:
        dict|None: A dictionary containing the game's details if successful, None otherwise
    """
    game_details = request(
        f'https://store.steampowered.com/api/appdetails?appids={app_id}',
        squelch=squelch or squelch_request, throw_error=throw_http_error,
    )
    if not game_details:
        if not squelch:
            print(f"Failed to retrieve data for app {app_id}")
        return None

    game_details = game_details[str(app_id)]
    if not game_details['success']:
        if not squelch:
            print(f"Data for app {app_id} not available")
        return None

    game_data = game_details['data']
    if not squelch:
        print(f"Retrieved details for {game_data['name']}")

    return game_data
