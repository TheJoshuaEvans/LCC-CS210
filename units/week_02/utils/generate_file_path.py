import os

def generate_file_path(file_path: str) -> str:
    """
    Generate an absolute file path relative to the `steam_recommendation.py` file - the entry point of
    this application. This allows the program to be run from any directory

    Args:
        file_path (str): The relative file path to convert to an absolute path
    Returns:
        str: The absolute file path
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(script_dir, '..', file_path)
    return os.path.realpath(file_path)
