from building_business import Business


class Office(Business):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_parking_lot, number_of_offices: int):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_parking_lot)
        self.number_of_offices = number_of_offices


if __name__ == '__main__':
    consulting = Office(100, 2, False, 'concrete', True, 4)

    print(consulting.has_parking_lot)
    print(consulting.description())
    print(consulting.number_of_offices)
