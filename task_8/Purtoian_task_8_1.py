def show_function_name(func):
    """Create a decorator that prints to the console the name of the
    function that was called.
    The function should work as intended.
    """
    def wrapper(*args, **kwargs):
        print("Called function:", func.__name__)
        return func(*args, **kwargs)
    return wrapper


@show_function_name
def summation(a, b):
    summ = a + b
    print(f"The result is: {summ}")
    return summ


@show_function_name
def multiplication(a, b):
    mult = a * b
    print(f"The result is: {mult}")
    return mult
