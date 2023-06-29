"""
Describe the Train object. The class must contain fields and a method
for adding wagons (it is necessary to add objects, and instances of
the wagon class). Describe the class Wagon together with the train.
The Wagon must contain a list of passengers and allow adding passengers.
In the Wagon can be 10 passengers for example. When using the
len function on a Wagon, I want to see the number of passengers.
When using len on a train, I want to see a list of Wagons without a
locomotive. Each wagon must have a number. When printing a wagon
to the console, I want to see the following "[n]" where n is the number
of the wagon.
***
Implement a train print from task 2. When you print a train, wagons and
a locomotive should be displayed in the console in the following format:
<=[HEAD]-[1]-[2]-[3]-[4]-[...]-[n]-[n-1]
"""


class Train:
    def __init__(self):
        self.__wagons = []

    def add_wagon(self, wagon):
        self.__wagons.append(wagon)

    def __len__(self):
        return len(self.__wagons)

    def __str__(self):
        wagon_list = '--'.join(str(wagon) for wagon in self.__wagons)
        return f"<=[HEAD]-{wagon_list}"


class Wagon:
    def __init__(self, number):
        self.__number = number
        self.__passengers = []

    def add_passenger(self, passenger):
        if len(self.__passengers) < 10:
            self.__passengers.append(passenger)
        else:
            raise ValueError("Wagon is full. Cannot add more passengers.")

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f"[{self.__number}]"


if __name__ == '__main__':
    train = Train()

    wagon1 = Wagon(1)
    wagon2 = Wagon(2)
    wagon3 = Wagon(3)
    wagon4 = Wagon(4)

    train.add_wagon(wagon1)
    train.add_wagon(wagon2)
    train.add_wagon(wagon3)
    train.add_wagon(wagon4)

    wagon1.add_passenger("Passenger 1")
    wagon1.add_passenger("Passenger 2")
    wagon1.add_passenger("Passenger 3")
    wagon1.add_passenger("Passenger 4")
    wagon1.add_passenger("Passenger 5")
    wagon1.add_passenger("Passenger 6")
    wagon2.add_passenger("Passenger 1")
    wagon2.add_passenger("Passenger 2")
    wagon3.add_passenger("Passenger 1")
    wagon3.add_passenger("Passenger 2")
    wagon3.add_passenger("Passenger 3")

    print(len(wagon1))
    print(len(wagon2))
    print(len(wagon3))
    print(len(wagon4))
    print("-------")
    print(wagon1)
    print(wagon2)
    print(wagon3)
    print(wagon4)
    print("-------")
    print(len(train))
    print("-------")
    print(train)
