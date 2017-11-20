from model_user import ModelUser
from view_user import ViewUser
from controller_malopolska_area_container import ControllerMalopolskaAreaContainer


class ControllerUser():

    def __init__(self):
        self.view = ViewUser()

    def validate_input(self, message):
        pass

    def start(self):
        pass

    def view_area_list(self):
        pass

    def get_top_areas_by_longest_name(self, top=3, area_type="city"):
        pass

    def get_top_areas_by_sub_units_count(self, top=1, area_type="county"):
        pass

    def get_area_belonging_to_more_than_one_category(self, appearences=2):
        pass

    def search_for_expression(self, expression):
        pass

    def get_user_name(self):
        pass

    def delete_user(self):
        pass
