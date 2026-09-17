from solution import find_kth_largest


def test_example1():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_example2():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_single_element():
    assert find_kth_largest([1], 1) == 1


def test_k_equals_length():
    assert find_kth_largest([7, 3, 5, 1], 4) == 1


def test_duplicates():
    assert find_kth_largest([2, 2, 2, 2], 3) == 2


def test_negative_numbers():
    assert find_kth_largest([-1, -2, -3, -4, -5], 2) == -2
