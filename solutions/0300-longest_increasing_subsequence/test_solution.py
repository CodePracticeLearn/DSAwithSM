from solution import length_of_lis


def test_example_case():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_all_increasing():
    assert length_of_lis([1, 2, 3, 4, 5]) == 5


def test_all_decreasing():
    assert length_of_lis([5, 4, 3, 2, 1]) == 1


def test_single_element():
    assert length_of_lis([42]) == 1


def test_duplicates():
    assert length_of_lis([2, 2, 2, 2]) == 1


def test_mixed():
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
