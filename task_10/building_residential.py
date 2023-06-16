from building import Building


class Residential(Building):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_garden: bool):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material)
        self.has_garden = has_garden

    @staticmethod
    def clean_garden():
        print("The garden looks clean now!")

    @staticmethod
    def clean_floors():
        print("All floors are clean.")

    def description(self):
        return "Residential Building"
