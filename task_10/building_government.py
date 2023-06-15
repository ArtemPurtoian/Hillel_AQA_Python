from building import Building


class Government(Building):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, department: str):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material)
        self.department = department

    def description(self):
        return "Government Building"
