def arrows_to_rotate(directions: str):
    """
    You are given a string representing a sequence of N arrows,
    each pointing in one of the four cardinal directions:
    up (^), down (v), left(<) or right (>).
    Write a function that, given a string S denoting the directions of
    the arrows, returns the minimum number of arrows that must be rotated
    to make them all point in the same direction
    """
    arrows = {'^': 0, 'v': 0, '<': 0, '>': 0}

    for arrow in directions:
        arrows[arrow] += 1

    max_arrows = max(arrows.values())
    min_rotations = len(directions) - max_arrows

    return min_rotations
