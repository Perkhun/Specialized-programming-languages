from abc import ABC, abstractmethod
from colorama import Fore
from enum import Enum
from tkinter import Tk, Frame, Label, Button, StringVar, Entry, OptionMenu, filedialog, messagebox, simpledialog

class Colors(Enum):
    RED = Fore.RED
    GREEN = Fore.GREEN
    BLUE = Fore.BLUE

class Figure3D(ABC):
    def __init__(self, character: str, color: Colors):
        #Initialize a Figure3D object

        if not isinstance(color, Colors) or len(character) != 1:
            raise ValueError("Invalid input for character or color")
        self._character = character
        self._color = color

    @abstractmethod
    def get_2d_representation(self) -> list: #Abstract method to get the 2D representation of the figure. 
                                             #Which reeturns list of strings representing the 2D representation
        pass

    @abstractmethod
    def get_3d_representation(self, scale: float = 1.0) -> str:#Abstract method to get the 3D representation of the figure. 
        #default scale (float): The scaling factor for the figure (default is 1.0). Which returns string representing the 3D representation
        pass

    @staticmethod
    def is_appropriate_character(character: str) -> bool:
       #Check if the provided character is appropriate for a figure
        return len(character) == 1

    def change_color(self, color: Colors) -> None:
        #Change the color of the figure

        self._color = color

    def change_character(self, character: str) -> None:
        #Change the character used to represent the figure

        if self.is_appropriate_character(character):
            self._character = character
        else:
            print("Invalid character. It should be a single character.")
