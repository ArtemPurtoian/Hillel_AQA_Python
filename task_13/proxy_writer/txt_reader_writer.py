from abstract_reader import Reader


class TxtReaderWriter(Reader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_file(self):
        """Reading a file."""
        with open(self.file_path, 'r') as file:
            text = file.read()
        print(text)
        return text

    def is_file_empty(self):
        """Checking weather a file is empty."""
        with open(self.file_path, 'r') as file:
            return not bool(file.read())

    def write_file(self, data: str):
        """
        Writing to a file if it is empty.
        If not - overwriting is forbidden.
        """
        if self.is_file_empty():
            with open(self.file_path, 'w') as file:
                file.write(data)
                print(f"Data written successfully.\n*******\n{data}")
            return True
        else:
            print("File is not empty! Overwriting is forbidden!"
                  "\nClear the file or create a new one.")
            return False


if __name__ == '__main__':
    txt_writer = TxtReaderWriter('data.txt')
    # txt_writer.read_file()
    test_data = txt_writer.write_file("Hola mis amigos!")
