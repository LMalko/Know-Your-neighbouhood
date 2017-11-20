class ModelMalopolskaArea():

    province = 12

    def __init__(self, name, unit, county, municipality, rgmi):
        self.name = name
        self.unit = unit
        self.county = county
        self.municipality = municipality
        self.rgmi = rgmi

    def display_area(self):
        return "{} which is {} from no.{} county, no.{} municipality, no.{} rgmi".format(self.name,
                                                                                         self.unit,
                                                                                         self.county,
                                                                                         self.municipality,
                                                                                         self.rgmi)
