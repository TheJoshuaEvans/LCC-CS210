import sys

from utils.get_game_data import get_game_data
from utils.get_steam_api_key import get_steam_api_key
from utils.read_json import read_json
from utils.request import request
from utils.write_json import write_json

CONFIG_PATH = './configs.json'
SQUELCH = True
SQUELCH_REQUEST = True

class ProgramData():
    """All the data used by the program and is initialized in the init() function"""
    def __init__(self):
        self.games:list[dict] = []
        self.game_details:list[dict] = []
        self.configs:object = {}
        self.api_key:str = '__REDACTED_API_KEY__'

def init() -> ProgramData:
    """
    Performed cached initialization. This will attempt to retrieve the user's owned games, and then the
    details for every game owned by the user. If the user owns a lot of games this can cause 429 (too
    many request) errors from the Steam API, so this function will skip any remaining games if an error
    occurs during the retrieval process. The list of owned games and game details are cached, so this
    function will be much faster on subsequent runs - or even perform no requests at all.
    """
    print('--- PERFORMING INITIALIZATION ---')
    program_data = ProgramData()

    print('Retrieving configs...')
    configs = read_json(CONFIG_PATH)
    if (not configs):
        print('No configs found, creating new configs...')
        configs = {
            'steam_id': input('Please enter your Steam ID: ').strip(),
        }

    steam_id = configs['steam_id']; print(f'Steam ID: {steam_id}') # OMG I didn't realize that was allowed
    print(f'Retrieved configs!\n')

    print('Retrieving Steam API key...')
    api_key = get_steam_api_key()
    print('Retrieved Steam API key!\n')

    print('Retrieving owned games...')
    data = request(
        f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&include_played_free_games=True&format=json',
        SQUELCH_REQUEST
    )
    if not data:
        print('Failed to retrieve owned games, program can not continue!')
        sys.exit(1)

    games = data['response'].get('games', [])
    print(f"Retrieved {len(games)} owned games!\n")

    print('Retrieving game details...')
    game_details = []
    #Note: this can take some time, depending on library size and cache availability, and may eventually hit rate limits
    try:
        for game in games:
            app_id = game['appid']
            game_details.append(get_game_data(app_id, SQUELCH, SQUELCH_REQUEST, throw_http_error=True))
    except Exception as e:
        print(f"An error occurred while retrieving game details:\n```\n{e}\n```\nSkipping remaining games...")
    print(f'Retrieved details for {len(game_details)} games!')
    print('--- INITIALIZATION COMPLETE ---\n\n')

    program_data.games = games
    program_data.game_details = game_details
    program_data.configs = configs
    program_data.api_key = api_key
    return program_data
