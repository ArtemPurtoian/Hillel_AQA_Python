def my_max(some_iterable):
    """
    Implement your own implementation of function max
    """
    max_value = some_iterable[0]
    for value in some_iterable:
        if value > max_value:
            max_value = value
    return max_value


def my_min(some_iterable):
    """
    Implement your own implementation of function min
    """
    min_value = some_iterable[0]
    for value in some_iterable:
        if value < min_value:
            min_value = value
    return min_value
