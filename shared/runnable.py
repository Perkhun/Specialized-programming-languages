from abc import ABC, abstractmethod

class Runnable(ABC):
    """Class that has run method to override"""
    @abstractmethod
    def run(self):
        """Main method that run logic of program. Should override"""
