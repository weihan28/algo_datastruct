from typing import Callable
from src.sorting.utils.util import itself, swap


def in_sort(arr: list, *, key: Callable = itself, reverse: bool = False):
    """Efficient Insertion Sort Implementation."""
    n = len(arr)
    return _in_sort(arr, 0, n, key=key, reverse=reverse)


def _in_sort(arr: list, lo: int, hi: int, *, key: Callable, reverse: bool):
    """ Sorts the array/list in-place and returns the sorted array itself.
    Args:
        arr: List to sort.
        lo: Lower index of the list to sort.
        hi: Upper index of the list to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    for i in range(lo + 1, hi):
        j = i
        while j > lo:
            key_j1, key_j, = key(arr[j - 1]), key(arr[j])
            comp_res = key_j1 > key_j if not reverse else key_j1 < key_j
            if comp_res:
                swap(arr, j - 1, j)
                j -= 1
            else:
                break
    return arr


"""
Comparison based
in-place
stable
online(placed at the back)

Time Complexity:
    best: O(n)      , when the list is already in order
    worst: O(n^2)   , when the list is in reverse sorted order

Invariant:
    list[0..i-1] is sorted
    each traversal puts the ith elem into its final place
"""
