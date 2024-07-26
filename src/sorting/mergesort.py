from typing import Callable
from src.sorting.utils.util import itself

"""
Top Down Recursive.
"""


def m_sort_td(arr: list, *, key: Callable = itself, reverse: bool = False):
    """Top-Down Merge Sort Implementation.

    Args:
        arr: List to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    if n <= 1:
        return arr

    temp = []
    for elem in arr:
        temp.append(elem)
    return _m_sort_td(arr, temp, 0, n, key=key, reverse=reverse)


def _m_sort_td(
        arr: list,
        temp: list,
        lo: int,
        hi: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """Recursively Sorts the temp array into arr.

    invariant:
        arr stores the result from the previous merge.
        list[lo...mid) is left
        list[mid...hi) is right

    Args:
        arr: List to store result.
        temp: List to sort.
        lo: Lower index of the list to sort.
        hi: Upper index of the list to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    if hi - lo <= 1:
        return arr

    mid = (lo + hi) // 2
    # switch the roles of arr and temp for O(n) space complexity.
    # sorts arr into temp.
    _m_sort_td(temp, arr, lo, mid, key=key, reverse=reverse)
    _m_sort_td(temp, arr, mid, hi, key=key, reverse=reverse)
    # merges the result in temp into arr.
    _merge(arr, temp, lo, mid, hi, key=key, reverse=reverse)
    return arr


def _merge(arr,
           temp,
           lo,
           mid,
           hi,
           *,
           key: Callable = itself,
           reverse: bool = False
           ):
    """ Merges the contents from temp into arr

    Args:
        arr: List to store result.
        temp: List to sort.
        lo: Lower index of the list to merge.
        mid: middle index of the left and right portions in temp.
        hi: Upper index of the list to merge.
    """
    idx = lo
    l_counter = lo
    r_counter = mid

    while l_counter < mid and r_counter < hi:
        key_l, key_r = key(temp[l_counter]), key(temp[r_counter])
        # left duplicate has priority to maintain stability
        comp_res = key_l <= key_r if not reverse else key_l >= key_r
        if comp_res:
            arr[idx] = temp[l_counter]
            l_counter += 1
        else:
            arr[idx] = temp[r_counter]
            r_counter += 1
        idx += 1

    while l_counter < mid:
        arr[idx] = temp[l_counter]
        l_counter += 1
        idx += 1

    while r_counter < hi:
        arr[idx] = temp[r_counter]
        r_counter += 1
        idx += 1


""" 
comparison based
stable

Time Complexity:
    best: O(n log n)
    worst: O(n log n)
    where n is the number of elements in the array, log n is the maximum recursive depth.

Space Complexity:
    O(n) for temp array.
"""

"""
Bottom Up Iterative.
"""


def m_sort_bu(arr: list, *, key: Callable = itself, reverse: bool = False):
    """Top-Down Merge Sort Implementation.

    Args:
        arr: List to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    if n <= 1:
        return arr
    temp = []
    for elem in arr:
        temp.append(elem)
    return _m_sort_bu(arr, temp, 0, n, key=key, reverse=reverse)


def _m_sort_bu(
        arr: list,
        temp: list,
        lo: int,
        hi: int,
        *,
        key: Callable,
        reverse: bool
):
    """Bottom Up Iterative Merge Sort

    Concept:
        View the initial list as sorted sub-lists of width 0(size 1).
        merge them continuously into larger and larger sub-lists until it is one whole sorted list.

    Args:
        arr: List to store result.
        temp: List to sort.
        lo: Lower index of the list to sort.
        hi: Upper index of the list to sort.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    n = hi - lo
    if n <= 1:
        return arr

    working = arr
    temp_arr = temp
    # keeps track of the working arr
    is_arr = False
    size = 1
    # merge all sub-lists in temp_arr into working.
    while size < n:
        # merge each sub-lists
        start = lo
        while start < hi:
            mid = min(start + size, hi)
            end = min(mid + size, hi)
            _merge(working, temp_arr, start, mid, end, key=key, reverse=reverse)
            start = end
        working, temp_arr = temp_arr, working
        is_arr = not is_arr
        size *= 2

    # the final result is in temp
    if not is_arr:
        for i in range(lo, hi):
            arr[i] = temp[i]
    return arr
