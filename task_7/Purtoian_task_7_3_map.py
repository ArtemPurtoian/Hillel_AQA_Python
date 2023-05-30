from typing import Callable, Iterable, Any


def custom_map(callback: Callable[[Any], bool], sequence: Iterable[Any]):
    """
    Implement your own implementation of the function map
    """
    mapped_items = []
    for item in sequence:
        mapped_items.append(callback(item))
    return mapped_items
