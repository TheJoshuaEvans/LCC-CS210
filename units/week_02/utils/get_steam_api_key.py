import os

api_key_missing_message = """========== WARNING ==========
Environment variable 'STEAM_API_KEY' is not set, retrieving the game list will fail if the data is not cached.
You can create or obtain an API key from https://steamcommunity.com/dev/apikey.
Once you have a key, you can set it in your environment as follows -

Unix/MacOS:
export STEAM_API_KEY={your_api_key_here}

Windows Command Prompt:
set STEAM_API_KEY={your_api_key_here}

PowerShell:
$env:STEAM_API_KEY="{your_api_key_here}"

Remember to replace {your_api_key_here} with your actual Steam API key. Also note that setting the
environment variable in this way will only last for the duration of your terminal session
========== WARNING =========="""

def get_steam_api_key() -> str:
    """
        Retrieves the Steam API key from the `'STEAM_API_KEY` environment variable. If the variable is not
        set, print a message explaining how to set it and return the "redacted key" string so that the
        cache will be used if available

        Returns:
            str: The Steam API key.
    """
    steam_api_key = '__REDACTED_API_KEY__'
    try:
        steam_api_key = os.environ['STEAM_API_KEY']
    except KeyError:
        print(api_key_missing_message)

    return steam_api_key
