from model_malopolska_area import ModelMalopolskaArea


class ControllerMalopolskaArea():

    def __init__(self, data):
        self.malopolska_areas = data
        self.set_areas_objects()

    def set_areas_objects(self):
        disregard_categories_list = 1
        # x[4], x[5], x[1], x[2], x[3] stand for name, unit type, county, municipality and rgmi respectively.
        self.malopolska_areas_objects = [ModelMalopolskaArea(x[4], x[5], x[1], x[2], x[3]) 
                                         for x in self.malopolska_areas[disregard_categories_list:]]

    def get_areas_objects(self):
        return self.malopolska_areas_objects
