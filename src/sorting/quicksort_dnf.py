from typing import Callable
from src.sorting.utils.util import itself, swap
from src.sorting.selection.quickselect import med_of_med


def q_sort_dnf(arr, *, key: Callable = itself, reverse: bool = False):
    """Quick Sort using DNF Partitioning Scheme with MOM.
    DNF: Dutch National Flag partitioning
    MOM: Median of Medians pivot selection

    Args:
        arr (list): list to be sorted
        key (Callable, optional): key function. Defaults to itself.
        reverse (bool, optional): reverse order. Defaults to False.
    """
    n = len(arr)
    return _q_sort_dnf(arr, 0, n, key=key, reverse=reverse)


def _q_sort_dnf(
        arr: list,
        lo: int,
        hi: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """Quick Sort using DNF Partitioning Scheme with MOM.

    Args:
        arr (list): list to be sorted
        lo (int): lower bound of the list to be sorted
        hi (int): upper bound of the list to be sorted 
        key (Callable, optional): key function. Defaults to itself.
        reverse (bool, optional): reverse order. Defaults to False.
    """
    if hi - lo <= 1:
        return arr

    pivot_elem = med_of_med(arr, lo, hi, key=key, reverse=reverse)
    p_left, p_right = _dnf_partition(arr, lo, hi, pivot_elem, key=key, reverse=reverse)
    _q_sort_dnf(arr, lo, p_left, key=key, reverse=reverse)
    _q_sort_dnf(arr, p_right + 1, hi, key=key, reverse=reverse)
    return arr


def _dnf_partition(
        arr: list,
        lo: int,
        hi: int,
        pivot_elem: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """
    invariant:
        list[0...i-1]<pivot
        list[i...j-1]=pivot
        list[k+1...hi-1]>pivot
    
    Args:
        arr (list): list to be partitioned
        lo (int): lower bound of the list to be partitioned
        hi (int): upper bound of the list to be partitioned
        pivot_elem : pivot element (the element, not the index)
        key (Callable, optional): key function. Defaults to itself.
        reverse (bool, optional): reverse order. Defaults to False. 
    """
    i = lo
    j = lo
    k = hi - 1
    key_p = key(pivot_elem)
    while j <= k:
        key_j = key(arr[j])
        if key_j < key_p if not reverse else key_j > key_p:
            swap(arr, i, j)
            i += 1
            j += 1
        elif key_j > key_p if not reverse else key_j < key_p:
            swap(arr, j, k)
            # do not increment j
            k -= 1
        else:
            j += 1
    return i, k


"""
in-place 

Time Complexity(DNF Partitioning):
    Best: O(n), when all items are the same.
    worst: O(n^2), when all unique and pivot is extreme.
    Note: with MOM pivot selection, worst case becomes O(n). 
            As median of medians is guaranteed to be between 30% and 70% of the list.
    

Time Complexity(MOM):
    O(n)

Total Time Complexity(Quick Sort):
    best=worst=avg=O(n log n)

Note: 
    worst case occurs when pivot is extreme.
    In practice, random pivot selection works just as well as MOM.
    As, randomising makes the worst case is very rare.
"""

"""Just for comparison.
Time Complexity of Naive Quick Sort(Using first element as pivot):
    best: O(n log n), when pivot is median.
    worst: O(n^2), when all unique and pivot is extreme.
    avg: O(n log n)
"""
