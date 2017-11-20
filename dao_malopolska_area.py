import csv


class DAOMalopolskaArea():

    def __init__(self, filename="malopolska_area.csv"):
        self.filename = filename
        self.import_data()

    def import_data(self):
        with open(self.filename, "r", encoding="utf_8") as myfile:
            self.imported_data = [line for line in myfile]

    def extract_imported_data(self):
        return self.imported_data

a = DAOMalopolskaArea()
print(a.extract_imported_data())