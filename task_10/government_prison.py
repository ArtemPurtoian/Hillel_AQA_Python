from building_government import Government


class Prison(Government):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, department, number_of_cells: int,
                 max_prisoners: int):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, department)
        self.number_of_cells = number_of_cells
        self.max_prisoners = max_prisoners

    def close_all_cells(self):
        print(f"All {self.number_of_cells} cells closed.")

    @staticmethod
    def call_reinforcements():
        print("Riot!!! The Special Weapons Attack Team has been "
              "notified!")


if __name__ == '__main__':
    odesa_prison = Prison(300, 3, True, 'concrete', 'Ministry of Justice', 100, 500)

    print(odesa_prison.building_material)
    print(odesa_prison.description())
    print(odesa_prison.building_area)
    print(odesa_prison.department)
    print(odesa_prison.number_of_floors)

    odesa_prison.close_all_cells()
    odesa_prison.call_reinforcements()
