inout_med_of_med= [
    ([1,3,2,4,5, 1,7,2,3,5, 1,0,9,0,4, 1,2], 3),
    ([1,3,2,4,5], 3),
    ([12], 12),
    ([1,1,1,1,1,1,2], 2)
]  # (input_list, expected_output)


inout_kth_order = [
    ([1], 0, 1),
    ([1,2,3,4,5,6,7,8,9,10], 9, 10),
    ([1,3,2,7,5,6,8,4,9,10], 9, 10),
    ([1,2,3,4,5,6,7,8,9,10], 7, 8),
    ([1,1,1,1,1,1,1,0], 0, 0)
]  # (input_list, k, expected_output)