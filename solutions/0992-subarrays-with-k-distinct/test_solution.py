from solution import subarrays_with_k_distinct


def test_example1():
    assert subarrays_with_k_distinct([1, 2, 1, 2, 3], 2) == 7


def test_example2():
    assert subarrays_with_k_distinct([1, 2, 1, 3, 4], 3) == 3


def test_alternating():
    assert subarrays_with_k_distinct([1, 2, 1, 2, 1], 2) == 10


def test_k1():
    assert subarrays_with_k_distinct([1, 1, 1], 1) == 6
