import csv


class DAOMalopolskaArea():

    def __init__(self, filename="malopolska_area.csv"):
        self.filename = filename

    def import_data(self):
        with open(self.filename, "r", encoding="utf_8") as myfile:
            self.imported_data = myfile

    def __extract_imported_data(self):
        return [line for line in self.imported_data]
