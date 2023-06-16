from building_business import Business


class Bank(Business):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_parking_lot, bank_name: str):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_parking_lot)
        self.bank_name = bank_name

    def change_name(self, new_name):
        print(f"{self.bank_name} was renamed to {new_name}!")
        self.bank_name = new_name


if __name__ == '__main__':
    privatbank = Bank(30, 1, False, 'bricks', True, 'Privat Bank')

    print(privatbank.building_area)
    print(privatbank.number_of_floors)
    print(privatbank.has_elevator)
    print(privatbank.building_material)
    print(privatbank.has_parking_lot)
    print(privatbank.bank_name)
    print(privatbank.description())

    privatbank.expand_area(50)
    print(privatbank.building_area)
    privatbank.stop_elevator()
    privatbank.change_name('PB')
