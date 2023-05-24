import math


def square(side):
    """
    Write a function square that takes 1 argument, the side of the square,
    and returns 3 values (using a tuple): the perimeter of the square,
    the area of the square, and the diagonal of the square.
    """
    perimeter = 4 * side
    area = side ** 2
    diagonal = math.sqrt(2) * side
    return perimeter, area, diagonal
