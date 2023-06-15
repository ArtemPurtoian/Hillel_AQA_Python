from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, building_area: int, number_of_floors: int,
                 has_elevator: bool, building_material: str):
        self.building_area = building_area
        self.number_of_floors = number_of_floors
        self.has_elevator = has_elevator
        self.building_material = building_material

    @abstractmethod
    def description(self):
        pass
