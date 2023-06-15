import datetime


class Employee:
    """Creating a class that describes an employee."""
    min_salary = 1000

    def __init__(self, first_name: str, last_name: str, age: int,
                 location: str, position: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__location = location
        self.__position = position

    @classmethod
    def change_min_salary(cls, new_salary: int | float):
        """
        Changing static class attribute min_salary in a classmethod.
        """
        if type(new_salary) in (int, float) and new_salary > 0:
            cls.min_salary = new_salary
        else:
            raise ValueError(f"The salary must be a positive number.")

    @classmethod
    def employee_salary(cls, experience: int):
        """Employee's salary based on experience."""
        if type(experience) == int:
            return cls.min_salary * experience / 1.6
        else:
            print(f"Employee's salary is reviewed every year.")

    @classmethod
    def from_string_hyphens(cls, string_hyphens: str):
        """
        Parsing a string with employee attributes separated
        by hyphens so that the hyphens be replaced with free spaces.
        """
        first_name, last_name, age, location, position = \
            string_hyphens.split('-')
        return cls(first_name, last_name, age, location, position)

    @staticmethod
    def workday(day):
        """
        Staticmethod which shows whether the current day is a workday
        or a day off.
        """
        if day.weekday() == 5 or day.weekday() == 6:
            return f"Day off!"
        return f"Workday!"

    @property
    def full_name(self):
        """
        Getting the full name out of the first and the last name.
        """
        if type(self.__first_name) == str and type(self.__last_name) == str:
            return f"{self.__first_name.title()} {self.__last_name.title()}"
        else:
            raise ValueError(f"Name must contain str only!")

    @full_name.setter
    def full_name(self, name: str):
        """
        Changing employee's first and last name out of the full name.
        """
        first_name, last_name = name.split(' ')
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def first_name(self):
        """Getting employee's first name."""
        return self.__first_name.title()

    @property
    def last_name(self):
        """Getting employee's last name."""
        return self.__last_name.title()

    @property
    def age(self):
        """Getting employee's age."""
        return self.__age

    @property
    def position(self):
        """Getting employee's position."""
        return self.__position.title()

    @position.setter
    def position(self, new_position: str):
        """Changing employee's position."""
        self.__position = new_position
        print(f"{self.full_name} is now the {self.__position.title()}.")

    @property
    def email(self):
        """
        Getting an email address out of the first and the last name.
        """
        return f"{self.__first_name}.{self.__last_name}@email.com"

    @property
    def show_location(self):
        """Getting employee's location."""
        return self.__location.title()

    def change_location(self, location: str):
        """
        Regular class method which changes the location and displays
        a message.
        """
        self.__location = location
        print(f"{self.full_name} relocated to {self.__location.title()}.")


if __name__ == '__main__':
    employee_1 = Employee('alex', 'johnson', 29, 'odesa', 'qa')
    print(employee_1.full_name)
    print('-----------')

    employee_1.full_name = 'john connor'
    print(employee_1.full_name)
    print(employee_1.email)
    print(employee_1.employee_salary(4))
    print('-----------')

    Employee.change_min_salary(1500)
    print(Employee.min_salary)
    print('-----------')

    employee_2 = Employee.from_string_hyphens('anna-simpson-30-kyiv-qa')
    print(employee_2.full_name)
    print(employee_2.first_name)
    print(employee_2.last_name)
    print(employee_2.email)
    print('-----------')

    my_date = datetime.date(2023, 6, 12)
    print(Employee.workday(my_date))

    employee_2.position = 'manager'
    employee_1.position = 'tech lead'

    print(employee_2.employee_salary(4))
    print(employee_2.show_location)
    employee_2.change_location('odesa')
