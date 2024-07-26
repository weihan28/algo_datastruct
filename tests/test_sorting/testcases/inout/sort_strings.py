""" Tests cases for sorting strings/characters in ascending order.
testcase = [..(input_list, output_list)..]
"""

""" Tests for stability characters"""
inout_stable_sort_by_first_elem_char = [
        ([('c', 0), ('d', 0), ('z', 0), ('g', 0), ('g', 1), ('f', 0), ('h', 0)],
         [('c', 0), ('d', 0), ('f', 0), ('g', 0), ('g', 1), ('h', 0), ('z', 0)])
]


""" Tests for sorting characters"""
inout_char = [
        (['c', 'a', 'b', 'z', 'x', 'm'], ['a', 'b', 'c', 'm', 'x', 'z']),         # Random order with characters
        (['a', 'b', 'c', 'm', 'x', 'z'], ['a', 'b', 'c', 'm', 'x', 'z']),         # Already sorted characters
        (['z', 'x', 'm', 'c', 'b', 'a'], ['a', 'b', 'c', 'm', 'x', 'z']),         # Descending order characters
        ([], []),                                                                 # Empty list of characters
        (['x'], ['x']),                                                           # List with 1 character
        (['x', 'a'], ['a', 'x']),                                                 # List with 2 characters
        (['a', 'x'], ['a', 'x']),                                                 # List with 2 characters sorted
        (['a', 'a'], ['a', 'a'])                                                  # List with 2 duplicate characters
]

""" Tests for sorting strings"""
inout_string_by_length = [
        ["apple", "banana", "kiwi", "orange", "grape"],
        ["kiwi", "apple",  "grape", "banana", "orange"]
]


inout_string_lexicographic = [
        (["app", "apple", "a", "z", "apply", "application"], 
         ['a', 'app', 'apple', 'application', 'apply', 'z']),

        ([], []),
        (["app"], ["app"]),
        (["ab", "a"], ["a", "ab"]),
        ([""], [""]),
        
        (["app", "apple", "a", "z", "apply", "", "application", ""],
         ['', '', 'a', 'app', 'apple', 'application', 'apply', 'z'])
]