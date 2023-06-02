def even_squares():
    """
    Create a function that can return the squares of even elements
    for the range 0 to 1000000000 inclusive.
    The solution should work and not freeze your computer.
    """
    number = 0
    while number <= 1000_000_000:
        if number % 2 == 0:
            yield number ** 2
        number += 1


squares = even_squares()
for element in range(101):
    square = next(squares)
    print(f"Number = {int(square ** 0.5)}, Square = {square}")
