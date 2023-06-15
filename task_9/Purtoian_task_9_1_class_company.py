class Company:
    """
    Creating a class that describes a company.
    """
    location = 'Sweden'

    def __init__(self, name: str, industry: str, income: int | float):
        self.__name = name
        self.__industry = industry
        self.__income = income
        self.__employees = []

    @classmethod
    def change_location(cls, new_location: str):
        """
        Changing the static 'location' class attribute and
        printing the corresponding message or raising an error if type
        is not string.
        """
        if type(new_location) == str:
            cls.location = new_location
            print(
                f"Our offices are now located in {new_location.title()}!")
        else:
            raise ValueError("Location must be of type string.")

    @classmethod
    def company_from_dict(cls, company_info: dict):
        """Alternative class constructor using a dictionary."""
        name = company_info.get("name")
        industry = company_info.get("industry")
        income = company_info.get("income")
        return cls(name, industry, income)

    @staticmethod
    def company_motto(motto: str):
        """Static method which prints a company motto."""
        print(f'"{motto}"')

    @property
    def name(self):
        """Getting the company name."""
        return self.__name.upper()

    @property
    def industry(self):
        """Getting the company industry."""
        return self.__industry.upper()

    @industry.setter
    def industry(self, new_industry: str):
        """Changing the company industry."""
        if type(new_industry) == str:
            self.__industry = new_industry
            print(f"The {self.name} is now in {self.industry}!")
        else:
            raise ValueError

    @property
    def income(self):
        """Getting company income."""
        return self.__income

    @income.setter
    def income(self, new_income: int | float):
        """Changing company income."""
        if type(new_income) in (int, float):
            self.__income = new_income
            print(f"The {self.name} has made €{self.__income}!")

    @property
    def employee_count(self):
        """Getting the number of employee's."""
        return self.__employees

    def add_employee(self, employee: str):
        """Adding an employee to the list of employees."""
        if type(employee) == str:
            self.__employees.append(employee)
        else:
            raise ValueError("Employee's name must be of string type.")

    def company_info(self):
        """Showing the full company info based on the attributes."""
        if 0 < len(self.__employees) < 5:
            print(f"The {self.name} - {self.__industry.upper()} "
                  f"company with {len(self.__employees)} employees.")
            print(f"It has €{self.__income} net income.")
            print(f"The company is actively hiring!")
        elif len(self.__employees) >= 5:
            print(f"The {self.name} - {self.__industry.upper()} "
                  f"company with {len(self.__employees)} employees.")
            print(f"It has €{self.__income} net income.")
            print(f"The company is not currently hiring.")
        else:
            print(f"The {self.name} is a startup.")
            print(f"It has €{self.__income} startup capital.")
            print(f"The {self.name} company has no employees "
                  f"yet.")


if __name__ == '__main__':
    Company.company_motto('Just Do It!')
    print('---------')
    my_company = Company("gentlemen's club", 'it', 50000)
    my_company.add_employee('adam')
    my_company.add_employee('john')
    my_company.add_employee('alex')
    my_company.add_employee('bob')
    my_company.add_employee('bob')

    my_company.company_info()
    print(my_company.employee_count)
    print(my_company.name)
    print(my_company.industry)
    print('---------')
    print(my_company.income)
    print(my_company.location)

    Company.change_location('great britain')
    print(my_company.location)
    my_company.industry = 'automotive'
    my_company.income = 150000
    my_company.company_info()
    print('---------')

    company_2 = {'name': 'ABC_Soft', 'industry': 'it', 'income': 10000}
    my_company_2 = Company.company_from_dict(company_2)
    my_company_2.company_info()
