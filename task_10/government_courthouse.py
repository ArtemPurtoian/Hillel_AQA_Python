from building_government import Government


class Courthouse(Government):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, department, number_of_courtrooms: int):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, department)
        self.number_of_courtrooms = number_of_courtrooms


if __name__ == '__main__':
    primorsky_courthouse = Courthouse(200, 3, False, 'aerated concrete', 'Judicial', 5)

    print(primorsky_courthouse.number_of_courtrooms)
    print(primorsky_courthouse.description())
    print(primorsky_courthouse.has_elevator)
    print(primorsky_courthouse.building_material)
