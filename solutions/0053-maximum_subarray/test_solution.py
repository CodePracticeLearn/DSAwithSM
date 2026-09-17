from solution import max_subarray

def test_example_mixed():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_single_element_positive():
    assert max_subarray([5]) == 5

def test_single_element_negative():
    assert max_subarray([-3]) == -3

def test_all_negative():
    assert max_subarray([-8, -3, -6, -2, -5, -4]) == -2

def test_all_positive():
    assert max_subarray([1, 2, 3, 4, 5]) == 15

def test_negative_then_large_positive():
    assert max_subarray([-1, -2, 10, -1, 10]) == 19
