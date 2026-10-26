from solution import rob


def test_example_basic():
    assert rob([1, 2, 3, 1]) == 4


def test_example_larger():
    assert rob([2, 7, 9, 3, 1]) == 12


def test_empty():
    assert rob([]) == 0


def test_single_house():
    assert rob([5]) == 5


def test_two_houses():
    assert rob([3, 10]) == 10


def test_all_equal():
    assert rob([5, 5, 5, 5, 5]) == 15


def test_alternating_high_low():
    assert rob([100, 1, 100, 1, 100]) == 300
