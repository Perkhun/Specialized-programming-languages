
"""Runner in facade pattern to run all subsystems"""
import unittest
from classes.lab1.main import main as lab1_main
from classes.lab2.main import main as lab2_main
from classes.lab3.main import main as lab3_main
from classes.lab4.main import main as lab4_main
from classes.lab5.main import main as lab5_main
import classes.lab6.test_calculator
from classes.lab7.main import main as lab7_main
from classes.lab8.main import main as lab8_main
from logs.logger import setup_logger, logger
from shared.console_input import UserInputHandler

class LabFacade:
    """Class for facade pattern"""
    @staticmethod
    def run_lab_1():
        """
        Run lab 2.
        """
        logger.info("Running lab 1")
        lab1_main()

    @staticmethod
    def run_lab_2():
        """
        Run lab 2.
        """
        logger.info("Running lab 2")
        lab2_main()

    @staticmethod
    def run_lab_3():
        """
        Run lab 3.
        """
        logger.info("Running lab 3")
        lab3_main()

    @staticmethod
    def run_lab_4():
        """
        Run lab 4.
        """
        logger.info("Running lab 4")
        lab4_main()

    @staticmethod
    def run_lab_5():
        """
        Run lab 5.
        """
        logger.info("Running lab 5")
        lab5_main()

    @staticmethod
    def run_lab_6():
        """
        Run lab 6.
        """
        unittest.main(classes.lab6.test_calculator)

    @staticmethod
    def run_lab_7():
        """
        Run lab 7.
        """
        logger.info("Running lab 7")
        lab7_main()

    @staticmethod
    def run_lab_8():
        """
        Run lab 8.
        """
        logger.info("Running lab 8")
        lab8_main()

if __name__ == "__main__":
    setup_logger()

    lab_facade = LabFacade()

    while True:
        lab_number = 0

        while True:
            lab_number = UserInputHandler.get_integer_input("Choose the lab number (1-8): ")
            if 0 <= lab_number <= 8:
                break
            else:
                print("Entered number does not correspond to any lab work (0-8)")

        if lab_number == 0:
            break
        else:
            getattr(lab_facade, f'run_lab_{lab_number}')()

        another_lab = UserInputHandler.get_yes_no_input("Do you want to perform another lab? (yes/no): ")
        if another_lab == 'no':
            break
