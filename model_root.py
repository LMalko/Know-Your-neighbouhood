from dao_malopolska_area import DAOMalopolskaArea


class ModelRoot():

    def __init__(self):
        self.malopolska_area_container = dao_malopolska_area.__extract_imported_data()
