from view_malopolska_area_container import ViewMalopolskaAreaContainer
from model_malopolska_area_container import ModelMalopolskaAreaContainer
from dao_malopolska_area import DAOMalopolskaArea
from controller_malopolska_area import ControllerMalopolskaArea
from model_malopolska_area import ModelMalopolskaArea


class ControllerMalopolskaAreaContainer():

    def __init__(self):
        self.associated_areas = DAOMalopolskaArea().extract_imported_data()
        self.associated_areas_objects = ControllerMalopolskaArea(self.associated_areas).get_areas_objects()
        self.ModelMalopolskaAreaContainer = ModelMalopolskaAreaContainer(self.associated_areas_objects)

    def get_collection_by_unit(self):
        return self.ModelMalopolskaAreaContainer.sort_units_count_by_size()

    def get_top_areas_by_longest_name(self):
        return [x.__str__() for x in self.ModelMalopolskaAreaContainer.set_top_areas_by_longest_name()]

    def get_top_county_by_number_of_municipalities(self):
        county_number = self.ModelMalopolskaAreaContainer.set_top_county_by_number_of_municipalities()
        return "".join([x.name for x in
                        self.associated_areas_objects if x.county == county_number and x.municipality == ""]).title()

    def get_areas_that_belong_to_more_than_one_category(self):
        return self.ModelMalopolskaAreaContainer.set_areas_that_belong_to_more_than_one_category()

    def get_search_for_expression_results(self, expression):
        return self.ModelMalopolskaAreaContainer.search_for_expression(expression.lower())

    def get_pprinted_collection_by_unit(self):
        return ViewMalopolskaAreaContainer().pprint_one_column_collection(self.get_collection_by_unit(), "MAŁOPOLSKIE")

    def get_pprinted_top_areas_by_longest_name(self):
        return ViewMalopolskaAreaContainer().pprint_lines(self.get_top_areas_by_longest_name(), "Top 3 cities")

    def get_pprinted_areas_that_belong_to_more_than_one_category(self):
        return ViewMalopolskaAreaContainer().pprint_lines(self.get_areas_that_belong_to_more_than_one_category(),
                                                          "Areas arranged by no. of categories, then alphabetically.")

    def get_pprinted_search_for_expression_results(self):
        pass





a = ControllerMalopolskaAreaContainer()
for i in a.associated_areas_objects:
    print(dir(i))
#print(a.get_search_for_expression_results("Nowy"))