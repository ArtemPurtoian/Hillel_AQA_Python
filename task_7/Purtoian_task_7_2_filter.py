from typing import Callable, Iterable, Any


def custom_filter(callback: Callable[[Any], bool], sequence: Iterable[Any]):
    """
    Implement your realization of the function filter
    """
    filtered_items = []
    for item in sequence:
        if callback(item):
            filtered_items.append(item)
    return filtered_items
