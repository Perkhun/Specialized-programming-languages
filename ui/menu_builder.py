from abc import ABC, abstractmethod


class Menu(ABC):
    """
    A description of the entire function, its parameters, and its return types.
    """

    @abstractmethod
    def run(self):
        """
        Abstract method to be implemented by subclasses.

        This method defines the behavior of the menu when it is executed.

        Raises:
            NotImplementedError: This method must be implemented by subclasses.
        """