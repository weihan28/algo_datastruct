from typing import Callable
from src.sorting.utils.util import itself

from src.sorting.countingsort import cnt_sort_digit


def rad_sort_int(arr: list, *, base: int = 10, key: Callable = itself, reverse: bool = False):
    """Radix Sort Implementation for positive integers of any length.

    Sorts positive integers of any length in any base.

    Pads Zeroes to the left of the number to make all numbers of the same length.(does not physically pad zeroes)
    Args:
        base: base of integer
        arr: List to sort.
        key: Key function to customize the sort order/extract the string to be used to sort.
        reverse: Flag to request the result in descending order.
    """
    n = len(arr)
    if n <= 1:
        return arr

    max_num = key(max(arr, key=key))
    # Align to the right
    i = 0
    while max_num // base ** i > 0:
        get_digit_key = lambda num: (key(num) // base ** i) % base
        cnt_sort_digit(arr, base, key=get_digit_key, reverse=reverse)
        i += 1
    return arr


"""
stable sort

Time Complexity:
    Worst = Best: O(k(m+n)) = O(k(base+n)) == O(kn)
    k: number of digits in the longest number

Space Complexity:
    O(m+n) = O(base + n) = O(n)

Note:
    radix sort is just doing counting sort for each digit(k times).
    time for counting sort is O(m+n) = O(base + n) = O(n)
    space for counting sort is O(m+n) = O(base + n) = O(n)
"""

"""
Note:
    We can use adjust bases to adjust time and space complexity.
    a bigger base will reduce the number of digits in the longest number, but increase the size of the count array.
        This makes the time faster.
    a smaller base will reduce the space complexity, but increase the number of digits in the longest number.
        This makes the space smaller.

    For example:
        we can do base 50 for base10 numbers to be able to sort it faster, but it will take more space(m=50).
        we can do base 2 for base10 numbers to be able to sort it with less space(m=2), but it will take more time.

        we can do base 10*2 for base10 numbers to be able to sort it with less space(m=20), 
        and it will take less time than base 2.
        Another way to see this is that we are doing counting sort for 2 columns at a time.
"""
