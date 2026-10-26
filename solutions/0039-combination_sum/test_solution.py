from solution import combination_sum


def test_example_basic():
    result = combination_sum([2, 3, 6, 7], 7)
    result_sorted = sorted([sorted(r) for r in result])
    expected = sorted([sorted(r) for r in [[2, 2, 3], [7]]])
    assert result_sorted == expected


def test_example_multiple_combinations():
    result = combination_sum([2, 3, 5], 8)
    result_sorted = sorted([sorted(r) for r in result])
    expected = sorted([sorted(r) for r in [[2, 2, 2, 2], [2, 3, 3], [3, 5]]])
    assert result_sorted == expected


def test_single_candidate_exact():
    result = combination_sum([3], 9)
    assert result == [[3, 3, 3]]


def test_single_candidate_no_solution():
    result = combination_sum([3], 7)
    assert result == []


def test_target_zero():
    result = combination_sum([1, 2, 3], 0)
    assert result == [[]]


def test_no_valid_combination():
    result = combination_sum([5, 10], 3)
    assert result == []
