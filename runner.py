import lab_work_1.main
import lab_work_2.main
import lab_work_3.main
import lab_work_4.main
from lab_5.main import FigureApp
import lab_work_6.test_calculator
import unittest


def get_integer_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return int(user_input)
        except ValueError:
            print("Please enter a valid integer.")


def get_yes_no_input(prompt):
    while True:
        user_input = input(prompt).lower()
        if user_input == 'yes' or user_input == 'no':
            return user_input
        else:
            print("Please enter 'yes' or 'no'")


if __name__ == "__main__":
    def choose_lab():
        while True:
            lab_number = get_integer_input("Choose the lab number (1-6): ")
            if 1 <= lab_number <= 6:
                return lab_number
            else:
                print("Entered number does not correspond to any lab work (1-6)")

    while True:
        lab_number = choose_lab()

        match lab_number:
            case 1:
                lab_work_1.main.main()
            case 2:
                lab_work_2.main.main()
            case 3:
                lab_work_3.main.main()
            case 4:
                lab_work_4.main.main()
            case 5:
                  # Create an instance of the FigureApp class
                figure_app = FigureApp()
              # Run the application
                figure_app.root.mainloop()
            case 6:
                unittest.main(lab_work_6.test_calculator)
            case 0:
                break

        another_lab = get_yes_no_input("Do you want to perform another lab? (yes/no): ")
        if another_lab == 'no':
            break
