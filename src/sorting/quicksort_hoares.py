from typing import Callable
from src.sorting.utils.util import itself, swap
import random


def q_sort_hoares(arr, *, key: Callable = itself, reverse: bool = False):
    """Quick Sort using Hoare's Partitioning Scheme.
    """
    n = len(arr)
    return _q_sort_hoares(arr, 0, n, key=key, reverse=reverse)


def _q_sort_hoares(
        arr: list,
        lo: int,
        hi: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    if hi - lo <= 1:
        return arr

    pivot_choice = random.randrange(lo, hi)
    pivot = _hoares_partition(arr, lo, hi, pivot_choice, key=key, reverse=reverse)
    # excludes pivot
    _q_sort_hoares(arr, lo, pivot, key=key, reverse=reverse)
    _q_sort_hoares(arr, pivot + 1, hi, key=key, reverse=reverse)
    return arr


def _hoares_partition(
        arr: list,
        lo: int,
        hi: int,
        pivot_choice: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """
    arr[lo..l-1] <= pivot
    arr[r+1..hi-1] > pivot
    """
    swap(arr, lo, pivot_choice)
    pivot = lo
    l_bad = lo + 1
    r_bad = hi - 1

    key_p = key(arr[pivot])
    while True:

        while l_bad <= r_bad:
            key_l = key(arr[l_bad])
            l_valid = key_l <= key_p if not reverse else key_l >= key_p
            if l_valid:
                l_bad += 1
            else:
                break

        while l_bad <= r_bad:
            key_r = key(arr[r_bad])
            r_valid = key_r > key_p if not reverse else key_r < key_p
            if r_valid:
                r_bad -= 1
            else:
                break

        if l_bad <= r_bad:
            swap(arr, l_bad, r_bad)
            # increment the counters as they dont include valid elems.
            l_bad += 1
            r_bad -= 1
        else:
            break
    swap(arr, lo, r_bad)
    return r_bad
