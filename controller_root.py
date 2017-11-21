from model_root import ModelRoot
from view_root import ViewRoot
from controller_user import ControllerUser
import sys


class ControllerRoot():

    def __init__(self):
        self.initialize_model()
        self.view = ViewRoot()

    def initialize_model(self):
        self.model = ModelRoot()

    def initialize_user_controller(self):
        return ControllerUser(self.user_name)

    def initialize_containers(self):
        self.malopolska_area_container = self.model.get_malopolska_area_container()

    def get_user_name(self):
        self.user_name = ViewRoot().display_login_screen()

    def menu_screen(self):
        self.menu_options = ModelRoot().get_menu_options()
        self.menu = ViewRoot().display_menu_screen(self.menu_options)

    def get_input(self, message):
        return ViewRoot().set_input(message)

    def get_message(self, message):
        return ViewRoot().display_message(message)

    def initialize_data(self):
        self.initialize_model()
        self.initialize_containers()
        self.get_user_name()
        self.user = self.initialize_user_controller()
        self.loop_through_menu()

    def return_data_according_to_menu_choice(self, root_input):
        if root_input == "1":
            return self.user.get_units_collection()
        elif root_input == "2":
            return self.user.get_top_areas_by_longest_name()
        elif root_input == "3":
            return self.get_message(self.user.get_top_county_by_number_of_municipalities())
        elif root_input == "4":
            return self.user.get_area_belonging_to_more_than_one_category()
        elif root_input == "5":
            root_input = self.get_input("Enter word/ expression You are looking for: ")
            return self.user.search_for_expression(root_input)
        elif root_input == "6":
            return self.user.get_areas_collection()
        elif root_input == "0":
            sys.exit()
        else:
            return self.get_message("No such choice")

    def loop_through_menu(self):
        while True:
            self.menu_screen()
            self.get_message("Hi, " + self.user_name + ". Choose your option")
            root_input = self.get_input("Option: ")
            ViewRoot().clear_screen()
            self.return_data_according_to_menu_choice(root_input)
            root_input = self.get_input("Press anything to continue.")
