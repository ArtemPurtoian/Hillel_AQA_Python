from building_residential import Residential


class House(Residential):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_garden, number_of_bedrooms: int,
                 has_swimming_pool: bool, has_garage: bool):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_garden)
        self.number_of_bedrooms = number_of_bedrooms
        self.has_swimming_pool = has_swimming_pool
        self.has_garage = has_garage


if __name__ == '__main__':
    my_house = House(70, 2, False, 'bricks', True, 3, True, True)

    print(my_house.has_swimming_pool)
    print(my_house.has_garage)
    print(my_house.description())
