from solution import search


def test_example_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example_not_found():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_element_found():
    assert search([1], 1) == 0


def test_single_element_not_found():
    assert search([1], 0) == -1


def test_not_rotated():
    assert search([1, 2, 3, 4, 5, 6, 7], 5) == 4


def test_rotated_target_in_left_half():
    assert search([4, 5, 6, 7, 0, 1, 2], 5) == 1


def test_target_at_boundaries():
    nums = [6, 7, 0, 1, 2, 3, 4, 5]
    assert search(nums, 6) == 0
    assert search(nums, 5) == 7
    assert search(nums, 0) == 2


def test_two_elements():
    assert search([2, 1], 1) == 1
    assert search([2, 1], 2) == 0
    assert search([2, 1], 3) == -1
