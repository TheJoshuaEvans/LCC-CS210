import json, os

from .generate_file_path import generate_file_path

def read_json(file_path: str) -> dict|None:
    """
    Reads a JSON file and returns its contents as a Python dictionary. If no data is found, None
    will be returned

    Args:
        file_path (str): The path to the JSON file relative to the `steam_recommendation.py` file.

    Returns:
        dict: The contents of the JSON file as a dictionary.
    """
    file_path = generate_file_path(file_path)

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except:
        return None
    return data
