from collections import Counter


class ModelMalopolskaAreaContainer():

    def __init__(self, area_container):
        self.area_container = area_container

    def count_areas_by_unit(self):
        return Counter([x.unit for x in self.area_container])

    def sort_units_count_by_size(self):
        self.areas_count = self.count_areas_by_unit()
        result = []
        result.append(("Liczba województw", self.areas_count["województwo"]))
        result.append(("Liczba powiatów", self.areas_count["powiat"]))
        result.append(("Liczba gmin miejskich", self.areas_count["gmina miejska"]))
        result.append(("Liczba gmin wiejskich", self.areas_count["gmina wiejska"]))
        result.append(("Liczba gmin miejsko-wiejskich", self.areas_count["gmina miejsko-wiejska"]))
        result.append(("Liczba obszarów wiejskich", self.areas_count["obszar wiejski"]))
        result.append(("Liczba miast", self.areas_count["miasto"]))
        result.append(("Liczba miast na prawach powiatu", self.areas_count["miasto na prawach powiatu"]))
        result.append(("Liczba delegatur", self.areas_count["delegatura"]))
        return result

    def set_top_areas_by_longest_name(self, top=3, area_type="city"):
        pass

    def set_top_areas_by_number_of_sub_units(self, top=1, area_type="county"):
        pass

    def set_area_that_belongs_to_more_than_one_category(self, appearences=2):
        pass

    def search_for_expression(self, expression):
        pass
