from solution import two_sum_ii


def test_example():
    assert two_sum_ii([2, 7, 11, 15], 9) == [1, 2]


def test_middle():
    assert two_sum_ii([2, 3, 4], 6) == [1, 3]


def test_two_elems():
    assert two_sum_ii([-1, 0], -1) == [1, 2]


def test_negatives():
    assert two_sum_ii([-3, -1, 0, 2, 4, 6], 3) == [1, 6]
