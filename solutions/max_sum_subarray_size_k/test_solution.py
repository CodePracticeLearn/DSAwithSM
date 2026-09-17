from solution import max_sum_subarray_k


def test_basic_example():
    assert max_sum_subarray_k([1, 2, 3, 4, 5], 3) == 12  # [3,4,5]


def test_single_element_window():
    assert max_sum_subarray_k([4, 1, 7, 2, 9], 1) == 9


def test_window_equals_array_length():
    assert max_sum_subarray_k([1, 2, 3], 3) == 6


def test_negative_numbers():
    assert max_sum_subarray_k([-1, -2, -3, -4], 2) == -3  # [-1,-2]


def test_mixed_numbers():
    assert max_sum_subarray_k([2, -1, 5, -3, 4, 1], 3) == 6  # [2,-1,5]


def test_k_too_large():
    assert max_sum_subarray_k([1, 2], 5) == 0


def test_k_zero():
    assert max_sum_subarray_k([1, 2, 3], 0) == 0
