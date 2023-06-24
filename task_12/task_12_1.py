"""
Describe any object of your choice in the class. I want the object
to be printed to the console in the following format:
class_name: {
key: value
}
"""


class Person:
    def __init__(self, name, age, occupation):
        self.__name = name
        self.__age = age
        self.__occupation = occupation

    def __str__(self):
        class_name = self.__class__.__name__
        attributes = {
            "name": self.__name,
            "age": self.__age,
            "occupation": self.__occupation
        }
        attributes_str = "\n".join([f"{key}: {value}" for key, value in attributes.items()])
        return f"{class_name}: {{\n{attributes_str}\n}}"


if __name__ == '__main__':
    person = Person("Artem Purtoian", 29, "QA")
    print(person)
