from solution import two_sum

def test_example_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_non_adjacent_elements():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_negative_numbers():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_elements():
    assert two_sum([1, 2], 3) == [0, 1]

def test_duplicates():
    assert two_sum([3, 3], 6) == [0, 1]

def test_large_numbers():
    assert two_sum([1000000, 500000, 500000], 1000000) == [1, 2]
