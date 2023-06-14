from building_residential import Residential


class ApartmentBuilding(Residential):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_garden, number_of_apartments: int):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_garden)
        self.number_of_apartments = number_of_apartments

    def number_of_apartments(self):
        return self.number_of_apartments


if __name__ == '__main__':
    london_aprt = ApartmentBuilding(300, 10, True, 'aerated concrete', True, 80)

    print(london_aprt.number_of_apartments)
    print(london_aprt.description())
