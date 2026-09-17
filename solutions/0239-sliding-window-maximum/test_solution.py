from solution import max_sliding_window


def test_example_case():
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]


def test_single_element_window():
    assert max_sliding_window([1, 2, 3, 4, 5], 1) == [1, 2, 3, 4, 5]


def test_window_equals_array_length():
    assert max_sliding_window([4, 2, 7, 1, 3], 5) == [7]


def test_all_same_elements():
    assert max_sliding_window([5, 5, 5, 5], 2) == [5, 5, 5]


def test_decreasing_sequence():
    assert max_sliding_window([9, 7, 5, 3, 1], 3) == [9, 7, 5]


def test_increasing_sequence():
    assert max_sliding_window([1, 3, 5, 7, 9], 3) == [5, 7, 9]
