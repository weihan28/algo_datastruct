from typing import Callable
from src.sorting.utils.util import itself


def key_low_case(ch):
    """ord(a..z) = 97..122  (unicode)"""
    # ord(ch)-ord('a')
    return ord(ch) - 97


def get_digit(n, base, digit):
    """ Extracts the digit from the number.

    Args:
        n: The number to extract the digit from.
        base: The base of the number.
        digit: The digit to extract(0,1,2,3..., from the left).
    """
    return (n // (base ** digit)) % base


def cnt_sort_lc_char(arr: list, key: Callable = itself, reverse: bool = False):
    """Counting Sort Implementation for lower case alphabets.

    Counting sort for lower case alphabets.
    Args:
        arr: List to sort.
        key: Key function to customize the sort order/extract the character to be used to sort.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    max_key = 25  # 26 alphabets (0..25)
    return _cnt_sort(arr, 0, n, max_key=max_key, key_count_arr=key_low_case, key=key, reverse=reverse)


def cnt_sort_digit(arr: list, base: int = 10, key: Callable = itself, reverse: bool = False):
    """Counting Sort Implementation for digits(of a particular base).

    Args:
        arr: List to sort.
        base: Base of the digits.
        key: Key function to customize the sort order/extract the digit to be used to sort.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    max_key = base - 1  # max_key does not include the base (0..9 for base 10).
    return _cnt_sort(arr, 0, n, max_key=max_key, key_count_arr=itself, key=key, reverse=reverse)


def cnt_sort_int(arr: list, key: Callable = itself, reverse: bool = False):
    """Counting Sort Implementation for integers.

    Args:
        arr: List to sort.
        key: Key function to customize the sort order/extract the integer to be used to sort.
        reverse: Flag to request the result in descending order.
    
    Note: Radix Sort solution is more efficient.
          since m can be significantly larger than n(m>>n).
          example: max_key = max(arr) = 10^9, where arr=[1,2,3,4,5,6,7,8,9,10^9]
    """
    n = len(arr)
    # only needs the max value of the key function, not the object containing the max value
    max_key = key(max(arr, key=key))
    return _cnt_sort(arr, 0, n, max_key=max_key, key_count_arr=itself, key=key, reverse=reverse)


""" Base Counting Sort Implementation.
Note: not optimized for radix sort.
"""


def _cnt_sort(
        arr: list,
        lo: int,
        hi: int,
        *,
        max_key: int,
        key_count_arr: Callable = itself,
        key: Callable = itself,
        reverse: bool = False
):
    """ Sorts the array/list and returns the sorted array itself.
    Args:
        arr: List to sort.
        lo: Lower index of the list to sort.
        hi: Upper index of the list to sort.
        max_key: The maximum possible value of the key function.
        key_count_arr: Key function to find the key of the elem in the count array.
        key: Key function to customize the sort order.
        reverse: Flag to request the result in descending order.
    """
    # count_array uses concept similar to separate chaining
    m = max_key + 1
    count_arr = [0] * m
    for i in range(m):
        count_arr[i] = []

    # populate the count array
    for i in range(lo, hi):
        count_arr[key_count_arr(key(arr[i]))].append(arr[i])

    # move back to array
    idx = lo
    sequence = range(m) if not reverse else reversed(range(m))
    for i in sequence:
        # count arr is FIFO, so the stability is preserved
        for j in range(len(count_arr[i])):
            arr[idx] = count_arr[i][j]
            idx += 1
    return arr


"""
Non-comparison based
stable

Time Complexity:
    best: O(n+m)    
    worst: O(n+m)  
    where n is the length of the list 
    where m is the range of the key function
        / max possible value of the key function
        / size of the count array

Space Complexity:
    O(n+m)

Things to note:
    m might be significantly larger than n(m>>n),
    in which case this algorithm is not efficient. 
    
    m is determined by the implementation of the key function.
"""

"""
Alternative Implementations of Counting Sort:

1. Count Array counts the number of occurrences of each key. 
Then populate the array with new elems based on the count array.

Pro: Size of the count array is O(m) instead os O(m+n). Since it only stores the number of occurrences.
Con: Not stable. It creates new elems instead of moving the existing elems.
"""
