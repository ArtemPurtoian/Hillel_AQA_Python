"""
Implement writer for proxy pattern from the lesson.
"""
from abstract_reader import Reader
from txt_reader_writer import TxtReaderWriter


class TxtProxyReaderWriter(Reader):
    def __init__(self, txt_path: str):
        self.__writer = TxtReaderWriter(txt_path)
        self.__txt_path = txt_path
        self.__is_admin = False
        self.__username = None
        self.__password = None

    def read_file(self):
        """Reading a file."""
        with open(self.__txt_path, 'r') as file:
            text = file.read()
        print(text)

    def __clear_file(self):
        """Making a file empty. Admin privilege."""
        with open(self.__writer.file_path, 'w') as file:
            file.truncate(0)

    def __append_to_file(self, data: str):
        """Appending data to a file. Admin privilege."""
        with open(self.__txt_path, 'a') as file:
            file.write("\n" + data)
            print(f"Data appended successfully.\n*******\n{data}")

    def write_file(self, data: str):
        """
        Writing to a file as admin. Inputting admin credentials lets to
        choose overwriting or appending to the existing data.
        Otherwise - access denied.
        """
        self.__username = input("Enter your username: ")
        self.__password = input("Enter your password: ")
        if self.__username == "admin" and self.__password == "admin":
            self.__is_admin = True
        else:
            self.__is_admin = False

        if self.__is_admin:
            print("Writing permission granted.")
            if self.__writer.is_file_empty():
                return self.__writer.write_file(data)
            else:
                overwrite = input("\nThe file is not empty."
                                  "\nDo you want to overwrite the file? "
                                  "(y/n): ")
                if overwrite.lower() == "y":
                    self.__clear_file()
                    self.__writer.write_file(data)
                elif overwrite.lower() == "n":
                    self.__append_to_file(data)
                else:
                    raise ValueError("Only 'y' or 'n' options available.")
        else:
            raise PermissionError("Access denied.")


if __name__ == '__main__':
    txt_proxy_writer = TxtProxyReaderWriter('data.txt')
    # txt_proxy_writer.read_file()
    test_data = txt_proxy_writer.write_file("Hello!" + "\nHi")
