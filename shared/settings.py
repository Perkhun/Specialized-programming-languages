"""
Settings module
"""
import json

CONFIG_FILE_PATH = 'config/config.json'

def load_config():
    """
    Load the configuration data from the specified file.

    Returns:
        dict: The configuration data loaded from the file.
              If the file is not found or there is an error decoding the JSON,
              an empty dictionary is returned.
    """
    try:
        with open(CONFIG_FILE_PATH, 'r', encoding='utf-8') as file:
            config_data = json.load(file)
        return config_data
    except FileNotFoundError:
        print(f"Config file '{CONFIG_FILE_PATH}' not found.")
        return {}
    except json.JSONDecodeError as exception:
        print(f"Error decoding JSON in config file: {exception}")
        return {}

def get_lab_settings(lab_name):
    """
    Retrieve the settings for a specific lab.

    Args:
        lab_name (str): The name of the lab.

    Returns:
        dict: The settings for the specified lab, or an empty dictionary if the lab is not found.
    """
    settings = load_config()
    return settings.get(lab_name, {})
