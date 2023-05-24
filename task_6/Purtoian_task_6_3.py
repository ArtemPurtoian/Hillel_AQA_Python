import math


def is_prime(number_for_prime):
    """
    Write a function is_prime that takes 1 argument - a number from 2 to 1000,
    and returns True if it is a prime number, and False otherwise
    """
    if number_for_prime < 2 or number_for_prime >= 1000:
        return False

    for current_number in range(2, int(math.sqrt(number_for_prime)) + 1):
        if number_for_prime % current_number == 0:
            return False

    return True
