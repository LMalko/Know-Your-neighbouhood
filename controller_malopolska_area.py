from model_malopolska_area import ModelMalopolskaArea


class ControllerMalopolskaArea():

    def __init__(self):
        self.malopolska_area = None

    def get_area_name(self, ModelMalopolskaArea):
        self.malopolska_area = ModelMalopolskaArea.display_area()

    def area_display(self, ModelMalopolskaArea):
        return self.malopolska_area
