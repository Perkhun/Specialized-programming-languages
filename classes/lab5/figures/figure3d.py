from abc import ABC, abstractmethod
from colorama import Fore
from enum import Enum

"""
Module Docstring: A brief description of the module.
"""
class Colors(Enum):
    RED = Fore.RED
    GREEN = Fore.GREEN
    BLUE = Fore.BLUE

class Figure3D(ABC):
    """
    Class Docstring: A brief description of the Figure3D class.
    """
    def __init__(self, character: str, color: Colors):
        #Initialize a Figure3D object
        """
        Initialize a Figure3D object.

        Parameters:
        - character (str): Character representing the figure.
        - color (Colors): Color of the figure.
        """
        if not isinstance(color, Colors) or len(character) != 1:
            raise ValueError("Invalid input for character or color")
        self._character = character
        self._color = color

    @abstractmethod
    def get_2d_representation(self) -> list: 
        """
        Abstract method to get the 2D representation of the figure.

        Returns:
        - list: List of strings representing the 2D representation.
        """
        pass

    @abstractmethod
    def get_3d_representation(self, scale: float = 1.0) -> str:
        """
        Abstract method to get the 3D representation of the figure.

        Parameters:
        - scale (float): Scaling factor for the figure (default is 1.0).

        Returns:
        - str: String representing the 3D representation.
        """
        pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:
        """
        Check if the provided character is appropriate for a figure.

        Parameters:
        - character (str): The character to check.

        Returns:
        - bool: True if the character is appropriate, False otherwise.
        """
        return len(character) == 1

    def change_color(self, color: Colors) -> None:
        """
        Change the color of the figure.

        Parameters:
        - color (Colors): New color for the figure.
        """
        self._color = color

    def change_character(self, character: str) -> None:
        """
        Change the character used to represent the figure.

        Parameters:
        - character (str): New character for the figure.

        Raises:
        - ValueError: If the character is not a single character.
        """
        if self.is_appropriate_character(character):
            self._character = character
        else:
            raise ValueError("Invalid character. It should be a single character.")
