import requests  # Importing requests module for making HTTP requests
from tkinter import messagebox  # Importing messagebox module from tkinter for displaying dialog boxes
from lab_work_7.message_box_wrapper import MessageBoxWrapper  # Importing MessageBoxWrapper class from a custom module

class APIHandler:
    base_url = 'https://jsonplaceholder.org/users'  # Base URL for the API

    @staticmethod
    def get_users():
        #Fetches a list of users from the API and returns a list of user data in JSON format.
       
        try:
            response = requests.get(APIHandler.base_url)  # Making a GET request to the API
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Parsing the JSON response and returning it
        except requests.exceptions.RequestException as e:
            MessageBoxWrapper.show_error("API Error", f'Error getting data from API: {e}')
            return []  # Returning an empty list in case of an error

    @staticmethod
    def get_user_by_id(user_id):
        #returns data in JSON format for the specified user ID.
       
        try:
            url = f'{APIHandler.base_url}/{user_id}'  # Constructing the URL for the specific user
            response = requests.get(url)  # Making a GET request to the API for the user
            response.raise_for_status()  # Raise an HTTPError for bad responses
            return response.json()  # Parsing the JSON response and returning it
        except requests.exceptions.RequestException as e:
            MessageBoxWrapper.show_error("API Error", f'Error getting user data from API: {e}')
            return {}  # Returning an empty dictionary in case of an error
