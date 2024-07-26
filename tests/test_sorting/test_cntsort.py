"""
Pytest module for testing the bsort module.
"""

import pytest
from tests.test_sorting.testcases.inout.sort_num import (
    inout_stable_sort_by_first_elem_digit,
    inout_stable_sort_by_first_elem_int,
)
from tests.test_sorting.testcases.inout.sort_strings import inout_stable_sort_by_first_elem_char
from tests.test_sorting.testcases.check_inout import check_inout

from src.sorting.countingsort import (cnt_sort_digit, cnt_sort_int, cnt_sort_lc_char)


# Test cnt_sort_digit
@pytest.mark.parametrize("input_list, expected_output", inout_stable_sort_by_first_elem_digit)
def test_stable_sort_by_first_elem_digit(input_list, expected_output):
    check_inout([(input_list, expected_output)], cnt_sort_digit, key=lambda x: x[0])


# Test cnt_sort_int
@pytest.mark.parametrize("input_list, expected_output", inout_stable_sort_by_first_elem_int)
def test_stable_sort_by_first_elem_int(input_list, expected_output):
    check_inout([(input_list, expected_output)], cnt_sort_int, key=lambda x: x[0])


# Test cnt_sort_lc_char
@pytest.mark.parametrize("input_list, expected_output", inout_stable_sort_by_first_elem_char)
def test_stable_sort_by_first_elem_char(input_list, expected_output):
    check_inout([(input_list, expected_output)], cnt_sort_lc_char, key=lambda x: x[0])
