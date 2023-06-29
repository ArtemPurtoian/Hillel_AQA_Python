from interfaces.i_elevator import IElevator
from time import sleep


# Elevator inherits from the abstract class IElevator
class Elevator(IElevator):
    # hiding
    def __init__(self, max_floors: int):
        self.__max_floors = max_floors
        self.__first_floor = 1

# Polymorphism allows to use all common methods
    def _current_floor(self, current_floor: int):
        """
        checking whether the current floor is valid
        """
        self.current_floor = current_floor
        if self.current_floor <= 0 or self.current_floor > self.__max_floors:
            raise ValueError(f"There is no {self.current_floor} floor.")
        else:
            print(f"You are on the {self.current_floor} floor.")

    def _call_elevator(self):
        """
        implementation and validation of calling the elevator
        """
        self.call = input("Press '0' to call the elevator. ")
        if self.call != '0':
            raise ValueError

    def _open_doors(self):
        """
        function which opens the doors
        """
        sleep(0.4)
        print("Opening the doors...")
        sleep(0.4)
        print("Elevator doors are opened.")

    def _close_doors(self):
        """
        function which closes the doors
        """
        sleep(0.4)
        print("Closing the doors...")
        sleep(0.4)
        print("Elevator doors are closed.")

    def _select_floor(self):
        """
        implementation and validation of the floor selection
        """
        self.end_floor = int(input("Select the floor. "))
        if self.current_floor == self.end_floor:
            print(f"You are already on the {self.end_floor} floor.")
            return self._select_floor()
        elif self.end_floor > self.__max_floors:
            raise ValueError(f"End floor can not be higher than "
                             f"{self.__max_floors}.")
        elif self.end_floor <= 0:
            raise ValueError(f"End floor can not be lower than "
                             f"{self.__first_floor}.")

    def _move_to_floor(self, current_floor: int):
        """
        implementation and validation of movement to the end floor
        """
        while current_floor != self.end_floor:
            if 0 < current_floor < self.end_floor <= self.__max_floors:
                current_floor += 1
                sleep(0.4)
                print(f"*** {current_floor} ***")
            else:
                # 0 < self.end_floor < current_floor <= self.__max_floors
                current_floor -= 1
                sleep(0.4)
                print(f"*** {current_floor} ***")

# Encapsulation of all methods that control operating an elevator
    def operate_elevator(self, current_floor: int):
        """
        encapsulating all methods within a single method,
        which coordinates the work of the entire class
        """
        self._current_floor(current_floor)
        self._call_elevator()
        self._open_doors()
        self._select_floor()
        self._close_doors()
        self._move_to_floor(current_floor)
        self._open_doors()
        self._close_doors()


if __name__ == '__main__':
    elevator = Elevator(10)
    elevator.operate_elevator(10)
