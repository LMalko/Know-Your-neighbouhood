from dao_malopolska_area import DAOMalopolskaArea


class ModelRoot():

    def __init__(self):
        self.imported_container_object = DAOMalopolskaArea().extract_imported_data()
        self.set_container_object()

    def set_container_object(self):
        self.malopolska_area_container = self.imported_container_object

    def get_malopolska_area_container(self):
        return self.malopolska_area_container

    def get_menu_options(self):
        self.menu_options = ["(1) List statistics",
                        "(2) Display 3 cities with longest names",
                        "(3) Display county's name with the largest number of communities",
                        "(4) Display locations, that belong to more than one category",
                        "(5) Advanced search",
                        "(0) Exit program"]
        return self.menu_options
