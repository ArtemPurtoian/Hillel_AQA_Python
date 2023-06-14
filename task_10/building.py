from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, building_area: int, number_of_floors: int,
                 has_elevator: bool, building_material: str):
        self.building_area = building_area
        self.number_of_floors = number_of_floors
        self.has_elevator = has_elevator
        self.building_material = building_material

    def building_area(self):
        return self.building_area

    def number_of_floors(self):
        return self.number_of_floors

    def has_elevator(self):
        return self.has_elevator

    def building_material(self):
        return self.building_material

    @abstractmethod
    def description(self):
        pass
