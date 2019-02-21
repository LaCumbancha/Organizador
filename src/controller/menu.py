from src.view.menu import ViewMenu

import os
from termcolor import colored


class Scheduler:

    def __init__(self):
        self._scheduler = Scheduler()
        self._view = ViewMenu()

    @staticmethod
    def _cls():
        os.system('cls' if os.name == 'nt' else 'clear')

    def main_menu(self):
        exit_value = False
        invalid = False

        while not exit_value:
            self._view.main_menu()
            if invalid:
                print(colored("Opción inválida. Reingrese.", "red"))
                invalid = False
            option = input()

            if option == "1":
                self._query_menu()
            elif option == "2":
                self._upload_menu()
            elif option == "3":
                self._cls()
            elif option == "4":
                self._scheduler.save()
                exit_value = True
            else:
                invalid = True
                self._cls()

    def _query_menu(self):
        exit_value = False
        invalid = False

        while not exit_value:
            self._view.query_menu()
            if invalid:
                print(colored("Opción inválida. Reingrese.", "red"))
                invalid = False
            option = input()

            if option == "1":
                self._grades_menu()
            elif option == "2":
                self._scheduler.credits()
            elif option == "3":
                self._scheduler.available_courses()
            elif option == "4":
                self._scheduler.passed_courses()
            elif option == "5":
                self._scheduler.academic_history()
            elif option == "6":
                exit_value = True
            else:
                invalid = True

    def _upload_menu(self):
        exit_value = False
        invalid = False

        while not exit_value:
            self._view.upload_menu()
            if invalid:
                print(colored("Opción inválida. Reingrese.", "red"))
                invalid = False
            option = input()

            if option == "1":
                self._scheduler.pass_course()
            elif option == "2":
                self._scheduler.remove_grade()
            elif option == "3":
                self._scheduler.fail_course()
            elif option == "4":
                exit_value = True
            else:
                invalid = True

    def _grades_menu(self):
        exit_value = False
        invalid = False

        while not exit_value:
            self._view.grades_menu()
            if invalid:
                print(colored("Opción inválida. Reingrese.", "red"))
                invalid = False
            option = input()

            if option == "1":
                self._scheduler.average_grades(with_cbc=False)
            elif option == "2":
                self._scheduler.average_grades(with_cbc=True)
            elif option == "3":
                exit_value = True
            else:
                invalid = True
