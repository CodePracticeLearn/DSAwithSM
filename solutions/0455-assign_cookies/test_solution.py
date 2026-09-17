from solution import find_content_children


def test_example_1():
    assert find_content_children([1, 2, 3], [1, 1]) == 1


def test_example_2():
    assert find_content_children([1, 2], [1, 2, 3]) == 2


def test_no_cookies():
    assert find_content_children([1, 2, 3], []) == 0


def test_no_children():
    assert find_content_children([], [1, 2, 3]) == 0


def test_all_children_satisfied():
    assert find_content_children([1, 1, 1], [3, 3, 3]) == 3


def test_no_child_satisfied():
    assert find_content_children([5, 6, 7], [1, 2, 3]) == 0


def test_single_child_single_cookie_match():
    assert find_content_children([3], [3]) == 1


def test_single_child_single_cookie_no_match():
    assert find_content_children([4], [3]) == 0


def test_large_greed_mixed():
    assert find_content_children([10, 9, 8, 7], [5, 6, 7, 8]) == 2
