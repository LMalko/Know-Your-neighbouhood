from model_user import ModelUser
from view_user import ViewUser
from controller_malopolska_area_container import ControllerMalopolskaAreaContainer


class ControllerUser():

    def __init__(self, username):
        self.view = ViewUser()
        self.controller_malopolska_area_container = ControllerMalopolskaAreaContainer()
        self.user = ModelUser(username)

    def get_units_collection(self):
        return self.controller_malopolska_area_container.set_pprinted_collection_by_unit()

    def get_areas_collection(self):
        return self.controller_malopolska_area_container.set_pprinted_all_areas_collection()

    def get_top_areas_by_longest_name(self):
        return self.controller_malopolska_area_container.set_pprinted_top_areas_by_longest_name()

    def get_top_county_by_number_of_municipalities(self):
        return self.controller_malopolska_area_container.get_top_county_by_number_of_municipalities()

    def get_area_belonging_to_more_than_one_category(self):
        return self.controller_malopolska_area_container.set_pprinted_areas_that_belong_to_more_than_one_category()

    def get_search_for_expression_results(self, expression):
        return self.controller_malopolska_area_container.set_pprinted_search_for_expression_results(expression)
