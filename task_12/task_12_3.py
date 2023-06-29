"""
Create an iterator that accepts a sequence and can iterate over values
over a given range. CustomIterator(sequence, start_index, end_index)
"""


class Iterator:
    def __init__(self, sequence, start_index, end_index):
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index
        self.__current_index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_index <= self.__end_index:
            value = self.__sequence[self.__current_index]
            self.__current_index += 1
            return value
        else:
            raise StopIteration()


if __name__ == '__main__':
    sequence_1 = range(1, 10)
    iterator_1 = Iterator(sequence_1, 1, 3)

    for element in iterator_1:
        print(element)
