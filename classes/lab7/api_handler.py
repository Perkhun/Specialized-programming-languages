"""
Module Docstring: A brief description of the module.
"""
import requests
from .message_box_wrapper import MessageBoxWrapper

class APIHandler:
    """
    A class for handling API requests.
    """
    base_url = 'https://jsonplaceholder.org/users'

    @staticmethod
    def get_users():
        """
        Get a list of users from the API.

        Returns:
            list: A list of user data dictionaries.
        """
        try:
            response = requests.get(APIHandler.base_url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            MessageBoxWrapper.show_error("API Error", f'Error getting data from API: {e}')
            return []

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get user data by user ID from the API.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            dict: A dictionary containing user data.
        """
        try:
            url = f'{APIHandler.base_url}/{user_id}'
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            MessageBoxWrapper.show_error("API Error", f'Error getting user data from API: {e}')
            return {}
