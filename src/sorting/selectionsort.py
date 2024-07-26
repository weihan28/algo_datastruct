from typing import Callable
from src.sorting.utils.util import itself, swap


def s_sort(arr: list, *, key: Callable = itself, reverse: bool = False):
    """Efficient Selection Sort Implementation.
    Args:
        arr: List to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    return _s_sort(arr, 0, n, key=key, reverse=reverse)


def _s_sort(arr: list, lo: int, hi: int, *, key: Callable, reverse: bool):
    """ Sorts the array/list in-place and returns the sorted array itself.
    Args:
        arr: List to sort.
        lo: Lower index of the list to sort.
        hi: Upper index of the list to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    for i in range(lo, hi):
        min_max = i  # index of the curr min/max elem
        for j in range(i+1, hi):
            key_j, key_min_max = key(arr[j]), key(arr[min_max])
            # if not reverse, min_max is the index of the min elem
            comp_res = key_j < key_min_max if not reverse else key_j > key_min_max
            if comp_res:  
                min_max = j
        swap(arr, i, min_max)
    return arr


"""
Comparison based
in-place

Time Complexity:
    best: O(n^2)    , when the list is in reverse sorted order
    worst: O(n^2)   , when the list is in reverse sorted order

Invariant:
    list[0..i-1] is in its final place.
    each traversal puts the unsorted part's min/max elem into its final place
"""