import re


def remove_numbers_from_file(input_file):
    """
    You have a file of unknown length. Write a function that will remove
    all numbers from each line of the file.
    """
    with open(input_file, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()

        for line in lines:
            no_numbers_line = re.sub(r'\d', ' ', line)
            file.write(no_numbers_line)
