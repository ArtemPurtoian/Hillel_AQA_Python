def display_box(width: int, height: int, character="*"):
    """
    Write a function with the following signature:
    def display_box(width: int, height: int, character="*") .
    This function will draw a simple ASCII-art rectangle (non-filled)
    of the given height and width, using character to print the lines.
    For example, display_box(5, 4, 'x') should output the following:
    xxxxx
    x   x
    x   x
    xxxxx
    """
    if width <= 0 or height <= 0:
        print("Width and height can not be 0 or negative.")

    top_and_bottom = character * width
    side = character + " " * (width - 2) + character

    print(top_and_bottom)
    for element in range(height - 2):
        print(side)
    print(top_and_bottom)
