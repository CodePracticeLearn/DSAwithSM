from solution import merge


def test_example_overlapping():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_example_contained():
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]


def test_single_interval():
    assert merge([[5, 7]]) == [[5, 7]]


def test_no_overlapping():
    assert merge([[1, 2], [3, 4], [5, 6]]) == [[1, 2], [3, 4], [5, 6]]


def test_all_overlapping():
    assert merge([[1, 10], [2, 5], [3, 7], [6, 8]]) == [[1, 10]]


def test_unsorted_input():
    assert merge([[8, 10], [1, 3], [2, 6], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_nested_intervals():
    assert merge([[1, 10], [2, 3], [4, 5], [6, 7]]) == [[1, 10]]
