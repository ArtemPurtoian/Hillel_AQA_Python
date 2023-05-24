def remove_vowels(input_string: str):
    """
    Write a function that takes in a string and returns the string
    with all the vowels removed.
    """
    vowels = 'aeiouAEIOU'
    no_vowels = ''
    for char in input_string:
        if char not in vowels:
            no_vowels += char
    return no_vowels
