from dao_malopolska_area import DAOMalopolskaArea


class ModelRoot():

    def __init__(self):
        self.imported_container_object = DAOMalopolskaArea().extract_imported_data()
        self.set_container_object()

    def set_container_object(self):
        self.malopolska_area_container = self.imported_container_object

    def get_malopolska_area_container(self):
        return self.malopolska_area_container
