from solution import average_subarrays_k

def test_basic_example():
    result = average_subarrays_k([1, 3, 2, 6, -1, 4, 1, 8, 2], 5)
    expected = [2.2, 2.8, 2.4, 3.6, 2.8]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-9

def test_k_equals_1():
    result = average_subarrays_k([4, 7, 2], 1)
    assert result == [4.0, 7.0, 2.0]

def test_k_equals_array_length():
    result = average_subarrays_k([1, 2, 3, 4], 4)
    assert len(result) == 1
    assert abs(result[0] - 2.5) < 1e-9

def test_empty_array():
    result = average_subarrays_k([], 3)
    assert result == []

def test_single_element():
    result = average_subarrays_k([5], 1)
    assert result == [5.0]

def test_negative_numbers():
    result = average_subarrays_k([-2, -4, -6, -8], 2)
    expected = [-3.0, -5.0, -7.0]
    assert len(result) == len(expected)
    for r, e in zip(result, expected):
        assert abs(r - e) < 1e-9
