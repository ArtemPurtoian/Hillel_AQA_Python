from building_business import Business


class Bank(Business):
    def __init__(self, building_area, number_of_floors, has_elevator,
                 building_material, has_parking_lot, bank_name: str):
        super().__init__(building_area, number_of_floors, has_elevator,
                         building_material, has_parking_lot)
        self.bank_name = bank_name

    def bank_name(self):
        return self.bank_name


if __name__ == '__main__':
    privatbank = Bank(30, 1, False, 'bricks', True, 'Privat Bank')

    print(privatbank.description())
    print(privatbank.building_area)
