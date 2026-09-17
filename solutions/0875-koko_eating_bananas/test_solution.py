from solution import min_eating_speed


def test_example1():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_example2():
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_example3():
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


def test_single_pile():
    assert min_eating_speed([10], 10) == 1


def test_single_pile_one_hour():
    assert min_eating_speed([10], 1) == 10


def test_all_ones():
    assert min_eating_speed([1, 1, 1, 1], 4) == 1


def test_large_h():
    # h equals total number of bananas, so k=1 suffices
    assert min_eating_speed([3, 6, 7, 11], 27) == 1
