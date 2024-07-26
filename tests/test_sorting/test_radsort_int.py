"""
Pytest module for testing the radix sort for positive integers
"""
import pytest
from tests.test_sorting.testcases.inout.sort_num import (
    inout_pos_num_large,
    inout_stable_sort_by_first_elem_pos_num_large
)
from tests.test_sorting.testcases.check_inout import check_inout

from src.sorting.radixsort_int import rad_sort_int

sort_func = rad_sort_int


# Test in base 10 for different lengths of positive integers
@pytest.mark.parametrize("input_list, expected_output", inout_pos_num_large)
def test_inout_pos_num_large(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)


# Test in base 10 for different lengths of positive integers with stability
@pytest.mark.parametrize("input_list, expected_output", inout_stable_sort_by_first_elem_pos_num_large)
def test_inout_stable_sort_by_first_elem_pos_num_large(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func, key=lambda x: x[0])


# Test in base 2 for different lengths of positive integers
@pytest.mark.parametrize("input_list, expected_output", inout_pos_num_large)
def test_inout_pos_num_large_base2(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func, base=2)


# Test in base 5 for different lengths of positive integers with stability
@pytest.mark.parametrize("input_list, expected_output", inout_stable_sort_by_first_elem_pos_num_large)
def test_inout_stable_sort_by_first_elem_pos_num_large_base5(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func, base=5, key=lambda x: x[0])
