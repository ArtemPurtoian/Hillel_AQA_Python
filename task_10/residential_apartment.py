from building_residential import Residential


class ApartmentBuilding(Residential):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_garden, number_of_apartments: int):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_garden)
        self.number_of_apartments = number_of_apartments

    @staticmethod
    def turn_on_security():
        print("Security system standby.")

    @staticmethod
    def alarm():
        print("Alarm! The police has been notified!")


if __name__ == '__main__':
    london_aprt = ApartmentBuilding(300, 10, True, 'aerated concrete', True, 80)

    print(london_aprt.number_of_apartments)
    print(london_aprt.description())
    london_aprt.turn_on_security()
    london_aprt.alarm()
