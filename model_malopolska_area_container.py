from collections import Counter


class ModelMalopolskaAreaContainer():

    def __init__(self, area_container):
        self.area_container = area_container

    def count_areas_by_unit(self):
        return Counter([x.unit for x in self.area_container])

    def sort_units_count_by_size(self):
        self.areas_count = self.count_areas_by_unit()
        return [("Liczba województw", self.areas_count["województwo"]),
                ("Liczba powiatów", self.areas_count["powiat"]),
                ("Liczba gmin miejskich", self.areas_count["gmina miejska"]),
                ("Liczba gmin wiejskich", self.areas_count["gmina wiejska"]),
                ("Liczba gmin miejsko-wiejskich", self.areas_count["gmina miejsko-wiejska"]),
                ("Liczba obszarów wiejskich", self.areas_count["obszar wiejski"]),
                ("Liczba miast", self.areas_count["miasto"]),
                ("Liczba miast na prawach powiatu", self.areas_count["miasto na prawach powiatu"]),
                ("Liczba delegatur", self.areas_count["delegatura"])]

    def set_top_areas_by_longest_name(self, top=3, area_type="miasto"):
        self.areas_wanted = [x for x in self.area_container if x.unit == area_type]
        return sorted(self.areas_wanted, key=lambda x: len(x.name), reverse=True)[0:top]

    def sort_counties_by_number_of_municipalities(self):
        return Counter([x.county for x in self.area_container])

    def set_top_county_by_number_of_municipalities(self):
        sorted_counties_by_subunits = self.sort_counties_by_number_of_municipalities()
        largest_county = sorted(sorted_counties_by_subunits.values(), key=lambda value: value, reverse=True)[0]
        for key, value in sorted_counties_by_subunits.items():
            if value == largest_county:
                return key

    def sort_cities_by_number_of_appearences(self):
        return Counter([x.name for x in self.area_container])

    def set_areas_that_belong_to_more_than_one_category(self, appearences=2):
        sort_cities_by_number_of_appearences = self.sort_cities_by_number_of_appearences()
        result = []
        for key, value in sort_cities_by_number_of_appearences.items():
            if value >= appearences:
                result.append("{} belongs to {} categories.".format(key, value))
        return result

    def search_for_expression(self, expression):
        return [x for x in self.area_container if expression in x.name.lower()]
