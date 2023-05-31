def my_all(some_iterable):
    """
    Implement your own all function
    """
    for element in some_iterable:
        if not element:
            return False
    return True
