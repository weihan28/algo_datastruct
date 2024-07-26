"""
This module contains a function to check the input and output of a sorting function.
Cannot be used for kth order statistics.
"""


def check_inout(inout, sort_func, **kwargs):
    """ Checks the input and output of a sorting function.
    inout: [(input_list, expected_output)..]
    sort_func: Sorting function to test.
    kwargs: Keyword arguments to pass to the sorting function.
    """
    for input_list, expected_output in inout:
        output = sort_func(input_list, **kwargs)
        assert output is not None, "Output should not be None"
        assert output == expected_output, f"Output: {output}, Expected: {expected_output}"