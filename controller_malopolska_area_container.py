from model_malopolska_area_container import ModelMalopolskaAreaContainer
from view_malopolska_area_container import ViewMalopolskaAreaContainer
from controller_malopolska_area import ControllerMalopolskaArea
from model_malopolska_area import ModelMalopolskaArea
from dao_malopolska_area import DAOMalopolskaArea


class ControllerMalopolskaAreaContainer():

    def __init__(self):
        self.associated_areas = DAOMalopolskaArea().extract_imported_data()
        self.associated_areas_objects = ControllerMalopolskaArea(self.associated_areas).get_areas_objects()
        self.ModelMalopolskaAreaContainer = ModelMalopolskaAreaContainer(self.associated_areas_objects)

    def get_collection_by_unit(self):
        return self.ModelMalopolskaAreaContainer.sort_units_count_by_size()

    def get_top_areas_by_longest_name(self):
        return [x.__str__() for x in self.ModelMalopolskaAreaContainer.get_top_areas_by_longest_name()]

    def get_top_county_by_number_of_municipalities(self):
        county_number = self.ModelMalopolskaAreaContainer.get_top_county_by_number_of_municipalities()
        return "".join([x.name for x in
                        self.associated_areas_objects if x.county == county_number and x.municipality == ""]).title()

    def get_areas_that_belong_to_more_than_one_category(self):
        return self.ModelMalopolskaAreaContainer.get_areas_that_belong_to_more_than_one_category()

    def get_search_for_expression(self, expression):
        return self.ModelMalopolskaAreaContainer.return_sorted_expression_findings(expression.lower())

    def set_pprinted_all_areas_collection(self):
        ViewMalopolskaAreaContainer().pprint_lines(sorted(self.associated_areas_objects, key=lambda x: x.name),
                                                   "All Malopolska Areas")

    def set_pprinted_collection_by_unit(self):
        ViewMalopolskaAreaContainer().pprint_one_column_collection(self.get_collection_by_unit(), "MAŁOPOLSKIE")

    def set_pprinted_top_areas_by_longest_name(self):
        ViewMalopolskaAreaContainer().pprint_lines(self.get_top_areas_by_longest_name(), "Top 3 cities")

    def set_pprinted_areas_that_belong_to_more_than_one_category(self):
        ViewMalopolskaAreaContainer().pprint_lines(self.get_areas_that_belong_to_more_than_one_category(),
                                                   "Areas arranged by no. of categories, then alphabetically.")

    def set_pprinted_search_for_expression_results(self, expression):
        ViewMalopolskaAreaContainer().pprint_two_columns_collection(self.get_search_for_expression(expression))
