import json

from pathlib import Path

from .generate_file_path import generate_file_path

def write_json(file_path: str, data: object) -> bool:
    """
    Writes a Python object to a JSON file. If there is an error, a message will be printed and False
    will be returned. Otherwise True will be returned

    Args:
        file_path (str): The path to the JSON file
        data (object): The data to write to the JSON file

    Returns:
        bool: True if the file was written successfully, False otherwise
    """
    try:
        file = Path(generate_file_path(file_path))
        file.parent.mkdir(parents=True, exist_ok=True)  # Ensure the directory exists

        with open(file, "w") as json_file:
            json.dump(data, json_file, indent=4)
    except IOError as e:
        print(f"Error writing to file: {e}")
        return False

    return True
