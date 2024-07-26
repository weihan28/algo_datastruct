"""
Pytest module for testing the quick select module.
"""

import pytest

from tests.test_sorting.testcases.inout.select_num import (inout_kth_order, inout_med_of_med)
from tests.test_sorting.testcases.check_inout import check_inout

from src.sorting.selection.quickselect import (q_select_dnf, med_of_med)


# test median of median
@pytest.mark.parametrize("input_list, expected_output", inout_med_of_med)
def test_stable_sort_by_first_elem_digit(input_list, expected_output):
    check_inout([(input_list, expected_output)], med_of_med, lo=0, hi=len(input_list))


# test quick_select
@pytest.mark.parametrize("input_list, k, expected_output", inout_kth_order)
def test_stable_sort_by_first_elem_digit(input_list, k, expected_output):
    output = q_select_dnf(input_list, k)
    assert output is not None, "Output should not be None"
    assert output == expected_output, f"Output: {output}, Expected: {expected_output}"
