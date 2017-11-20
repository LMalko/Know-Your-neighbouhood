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

    def get_area_name(self):
        pass

    def area_display(self):
        pass

    def get_collection_by_unit(self):
        return self.ModelMalopolskaAreaContainer.sort_units_count_by_size()

    def get_top_areas_by_longest_name(self):
        return [x.set_area() for x in self.ModelMalopolskaAreaContainer.set_top_areas_by_longest_name()]

    def get_top_county_by_number_of_municipalities(self):
        county_number = self.ModelMalopolskaAreaContainer.set_top_county_by_number_of_municipalities()
        return "".join([x.name for x in
                        self.associated_areas_objects if x.county == county_number and x.municipality == ""]).title()

    def get_areas_that_belong_to_more_than_one_category(self):
        return self.ModelMalopolskaAreaContainer.set_areas_that_belong_to_more_than_one_category()

    def get_search_for_expression_results(self, expression):
        return self.ModelMalopolskaAreaContainer.search_for_expression(expression.lower())




a = ControllerMalopolskaAreaContainer()
'''
for i in a.associated_areas_objects:
    print(i.set_area())'''
'''print(a.get_collection_by_unit())'''
#print(a.get_top_areas_by_longest_name())
#print(a.get_top_county_by_number_of_municipalities())
#print(a.get_areas_that_belong_to_more_than_one_category())
print(a.get_search_for_expression_results("Nowy"))