"""
Main module for running the FigureApp.

This module contains the main function to run the FigureApp, which creates an instance
of FigureApp and runs it.

Author: Ira
"""
from ui.menu.lab5.ui_lab5 import FigureApp

def main():
    """
    Main function to run the FigureApp.

    This function creates an instance of FigureApp and runs it.

    Raises:
        None
    """
    app = FigureApp()
    app.run()

if __name__ == "__main__":
    main()
