from typing import Callable
from src.sorting.utils.util import itself, swap

from src.sorting.insertionsort import _in_sort


def q_select_dnf(arr: list, k: int, *, key: Callable = itself, reverse: bool = False):
    """Quick Select using DNF Partitioning Scheme with MOM.

    Precondition:
        0 <= k < len(arr)
        arr is non-empty
    
    Args:
        arr (list): list to be sorted
        k (int): kth order(0-based)
        key : key function to extract value from element
        reverse : reverses the order if True
    """
    n = len(arr)
    assert n > 0, "list shouldn't be empty"
    return _q_select_dnf(arr, 0, n, k, key=key, reverse=reverse)


def _q_select_dnf(
        arr: list,
        lo: int,
        hi: int,
        k: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """ Quick Select using DNF Partitioning Scheme with MOM.

    Precondition:
        lo <= k < hi
        arr is non-empty

    Args:
        arr (list): list to be sorted
        lo (int): lower bound of the list to be sorted
        hi (int): upper bound of the list to be sorted 
        k (int): kth order(0-based)
        key : key function to extract value from element
        reverse : reverses the order if True    
    """
    assert lo <= k < hi, f"k:{k} should be between lo:{lo} and hi:{hi}, arr:{arr}"
    if hi - lo == 1:
        return arr[k]

    pivot_val = med_of_med(arr, lo, hi, key=key, reverse=reverse)
    p_left, p_right = _dnf_partition(arr, lo, hi, pivot_val, key=key)
    if k < p_left:
        return _q_select_dnf(arr, lo, p_left, k, key=key, reverse=reverse)
    elif k > p_right:
        return _q_select_dnf(arr, p_right + 1, hi, k, key=key, reverse=reverse)
    else:
        return arr[k]


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


def med_of_med(
        arr: list,
        lo: int,
        hi: int,
        *,
        key: Callable = itself,
        reverse: bool = False
):
    """Median of Medians.

    Args:
        arr (list): list to determine the median of medians
        lo (int): lower bound of the list 
        hi (int): upper bound of the list
        key : key function to extract value from element
        reverse : reverses the order if True
    """
    if hi - lo <= 5:
        _in_sort(arr, lo, hi, key=key, reverse=reverse)
        return arr[(hi + lo) // 2]

    curr = lo
    for i in range(lo, hi, 5):
        sublist_hi = min(i + 5, hi)
        sublist_med = (i + sublist_hi) // 2
        # the median of each group iis moved to the front of the list.
        # quick select is will move the kth item to the kth position.
        _q_select_dnf(arr, i, sublist_hi, sublist_med, key=key, reverse=reverse)
        swap(arr, curr, sublist_med)
        curr += 1
    return _q_select_dnf(arr, lo, curr, k=(lo + curr) // 2, key=key, reverse=reverse)


"""
space complexity:
    O(1) for median of medians
    O(1) for dnf partitioning
    O(1) for quick select
    O(log n) for recursion stack(considered in-place)

    
Time Complexity:
    O(n) for median of medians
    O(n) for dnf partitioning
    O(n) for quick select   
    O(n) in total


Median of Medians (MOM):
    1. Divide the list into n/5 groups of 5 elements each
    2. Find the median of each group by sorting(insertion sort of size 5) and select the median of medians
    3. Use the median of medians as the pivot
    4. Partition the list into 3 parts:
        list[lo..left-1] < pivot
        list[left..right] == pivot
        list[right+1..hi] > pivot

    Insertion sort -> O(5)=O(1) for each group. O(n/5) groups -> O(n)
    find the median of medians -> O(n/5)


dnf partitioning scheme partition the list into 3 parts:
        list[lo..left-1] < pivot
        list[left..right] == pivot
        list[right+1..hi] > pivot
"""
