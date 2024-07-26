from typing import TypeVar
T = TypeVar('T')


def itself(elem: T) -> T:
    """Identity function used for comparing."""
    return elem


def swap(arr: list[T], i: int, j: int) -> None:
    """Swap the values of 2 indices of a list."""
    arr[i], arr[j] = arr[j], arr[i]