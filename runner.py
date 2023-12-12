import lab_work_1.main
import lab_work_2.main
import lab_work_3.main
import lab_work_4.main
import lab_5.main
import lab_work_6.test_calculator
import unittest
import lab_work_7.main
import lab_work_8.main

class LabFacade:
    @staticmethod
    def run_lab_1():
        lab_work_1.main.main()

    @staticmethod
    def run_lab_2():
        lab_work_2.main.main()

    @staticmethod
    def run_lab_3():
        lab_work_3.main.main()

    @staticmethod
    def run_lab_4():
        lab_work_4.main.main()

    @staticmethod
    def run_lab_5():
        lab_5.main.main()

    @staticmethod
    def run_lab_6():
        unittest.main(lab_work_6.test_calculator)

    @staticmethod
    def run_lab_7():
        lab_work_7.main.main()

    @staticmethod
    def run_lab_8():
        lab_work_8.main.main()    



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
            lab_number = get_integer_input("Choose the lab number (1-8): ")
            if 0 <= lab_number <= 8:
                return lab_number
            else:
                print("Entered number does not correspond to any lab work (0-8)")

    lab_facade = LabFacade()

    while True:
        lab_number = choose_lab()

        if lab_number == 0:
            break
        else:
            getattr(lab_facade, f'run_lab_{lab_number}')()

        another_lab = get_yes_no_input("Do you want to perform another lab? (yes/no): ")
        if another_lab == 'no':
            break
