from dao_malopolska_area import DAOMalopolskaArea


class ModelRoot():

    def __init__(self):
        self.malopolska_area_container = DAOMalopolskaArea().extract_imported_data()

    def get_malopolska_area_container(self):
        return self.malopolska_area_container

    def get_menu_options(self):
        self.menu_options = ["(1) List statistics",
                             "(2) Display 3 cities with longest names",
                             "(3) Display county's name with the largest number of communities",
                             "(4) Display locations, that belong to more than one category",
                             "(5) Advanced search",
                             "(6) Show all areas",
                             "(0) Exit program"]
        return self.menu_options
