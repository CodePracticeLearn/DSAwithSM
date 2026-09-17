from solution import subarray_sum


def test_example():
    assert subarray_sum([1, 1, 1], 2) == 2


def test_example2():
    assert subarray_sum([1, 2, 3], 3) == 2


def test_negatives():
    assert subarray_sum([1, -1, 1, -1, 1], 0) == 6


def test_all_zeros():
    assert subarray_sum([0, 0, 0], 0) == 6


def test_single():
    assert subarray_sum([1], 1) == 1
    assert subarray_sum([1], 0) == 0
