from typing import Callable
from src.sorting.utils.util import itself, swap


def b_sort(arr, *, key: Callable = itself, reverse: bool = False):
    """Efficient Bubble Sort implementation.
    Sorts the array/list in-place and returns the sorted array itself.

    A custom key function can be supplied to customize the sort order, 
    and the reverse flag can be set to request the result in descending order.
    """
    n = len(arr)
    for marker in reversed(range(1, n)):
        swapped = False
        for j in range(marker):
            key_j, key_j1 = key(arr[j]), key(arr[j + 1])
            comp_res = key_j > key_j1 if not reverse else key_j < key_j1
            if comp_res:
                swap(arr, j, j + 1)
                swapped = True
        if not swapped:
            break
    return arr


"""
Comparison based

in-place
stable
online(place new elem at the front)

Time Complexity:
    best: O(n)      , when the list is already in order
    worst: O(n^2)   , when the list is in reverse sorted order

Invariant:
    list[marker+1..n-1] is in their final place.
    Each traversal puts the largest/smallest unsorted elem into its final place.
    Breaks early when no swaps occurred(is already sorted.)
"""
