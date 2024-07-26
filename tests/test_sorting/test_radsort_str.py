"""
Pytest module for testing the radix_sort for strings.
"""

import pytest
from tests.test_sorting.testcases.inout.sort_strings import inout_string_lexicographic
from tests.test_sorting.testcases.check_inout import check_inout

from src.sorting.radixsort_str import rad_sort_str

sort_func = rad_sort_str


@pytest.mark.parametrize("input_list, expected_output", inout_string_lexicographic)
def test_stable_sort_by_first_elem_digit(input_list, expected_output):
    check_inout([(input_list, expected_output)], sort_func)
