""" Tests cases for sorting numbers in ascending order.
testcase = [...(input_list, output_list)...]
"""


""" Tests for stability """
inout_stable_sort_by_first_elem_digit = [
        ([(4,'a'), (2,'a'), (7,'a'), (1,'a'), (1,'b'), (9,'a'), (5,'a')],
         [(1,'a'), (1,'b'), (2,'a'), (4,'a'), (5,'a'), (7,'a'), (9,'a')])
] 

inout_stable_sort_by_first_elem_int = [
        ([(14, 0), (12, 0), (17, 0), (11, 0), (11, 1), (19, 0), (15, 0)], 
         [(11, 0), (11, 1), (12, 0), (14, 0), (15, 0), (17, 0), (19, 0)])
]

""" Tests for sorting """
inout_pos_integers = [
        ([4, 2, 7, 1, 9, 5], [1, 2, 4, 5, 7, 9]),    # Random order
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),          # Already sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),          # Descending order
        ([], []),                                    # Empty list
        ([2], [2]),                                  # List with 1 item
        ([2, 1], [1, 2]),                            # List with 2 items (unsorted)
        ([1, 2], [1, 2]),                            # List with 2 items (sorted)
        ([1, 1], [1, 1])                             # List with 2 duplicate items
]


inout_neg_integers = [
        ([4, -2, 7, -1, 9, -5], [-5, -2, -1, 4, 7, 9]),        # Random order with negative integers
        ([-5, -2, -1, 4, 7, 9], [-5, -2, -1, 4, 7, 9]),        # Already sorted negative integers
        ([-1, -2, -3, -4, -5], [-5, -4, -3, -2, -1]),          # Descending order with negative integers
        ([], []),                                              # Empty list
        ([-2], [-2]),                                          # List with 1 item
        ([-1, -2], [-2, -1]),                                  # List with 2 items
        ([-2, -1], [-2, -1]),                                  # List with 2 items sorted
        ([-1, -1], [-1, -1])                                   # List with 2 duplicate items
]


inout_pos_floats = [
        ([4.2, 2.0, 7.5, 1.1, 9.9, 5.3], [1.1, 2.0, 4.2, 5.3, 7.5, 9.9]),      # Random order with positive floats
        ([1.1, 2.0, 4.2, 5.3, 7.5, 9.9], [1.1, 2.0, 4.2, 5.3, 7.5, 9.9]),      # Already sorted positive floats
        ([9.9, 7.5, 5.3, 4.2, 2.0, 1.1], [1.1, 2.0, 4.2, 5.3, 7.5, 9.9]),      # Descending order positive floats
        ([], []),                                                              # Empty list of positive floats
        ([2.5], [2.5]),                                                        # List with 1 positive float
        ([2.5, 1.1], [1.1, 2.5]),                                              # List with 2 positive floats
        ([1.1, 2.5], [1.1, 2.5]),                                              # List with 2 positive floats sorted
        ([1.1, 1.1], [1.1, 1.1])                                               # List with 2 duplicate positive floats
]


inout_neg_floats = [
        ([-4.2, -2.0, 7.5, 1.1, -9.9, -5.3], [-9.9, -5.3, -4.2, -2.0, 1.1, 7.5]),      # Random order with negative floats
        ([-9.9, -7.5, -5.3, -4.2, -2.0, -1.1], [-9.9, -7.5, -5.3, -4.2, -2.0, -1.1]),  # Already sorted negative floats
        ([-1.1, -2.0, -4.2, -5.3, -7.5, -9.9], [-9.9, -7.5, -5.3, -4.2, -2.0, -1.1]),  # Descending order negative floats
        ([], []),                                                                      # Empty list of negative floats
        ([-2.5], [-2.5]),                                                              # List with 1 negative float
        ([-1.1, -2.5], [-2.5, -1.1]),                                                  # List with 2 negative floats
        ([-2.5, -1.1], [-2.5, -1.1]),                                                  # List with 2 negative floats sorted
        ([-1.1, -1.1], [-1.1, -1.1])                                                   # List with 2 duplicate negative floats
]

# Test cases for sorting lists of large positive integers
inout_pos_num_large = [
        ([123,31232,12313123,4412313,44,1,21123], [1,44,123,21123,31232,4412313,12313123]),
        ([1111,1,11111,1,22,11,3], [1,1,3,11,22,1111,11111]),
]

inout_stable_sort_by_first_elem_pos_num_large = [
        ([(123, 0), (12141231231, 0), (32, 0), (1, 0), (0, 0), (123, 1), (32, 1)],
         [(0, 0), (1, 0), (32, 0), (32, 1), (123, 0), (123, 1), (12141231231, 0)])
]