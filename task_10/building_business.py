from building import Building


class Business(Building):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_parking_lot: bool):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material)
        self.has_parking_lot = has_parking_lot

    def expand_area(self, new_area):
        print(f"Our commercial building area was expanded to {new_area}.")
        self.building_area = new_area

    def description(self):
        return "Commercial Building"
