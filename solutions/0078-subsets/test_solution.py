from solution import subsets


def test_example_case():
    result = subsets([1, 2, 3])
    expected = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])


def test_empty_input():
    result = subsets([])
    assert result == [[]]


def test_single_element():
    result = subsets([5])
    expected = [[], [5]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])


def test_two_elements():
    result = subsets([0, 1])
    expected = [[], [0], [1], [0, 1]]
    assert sorted([sorted(s) for s in result]) == sorted([sorted(s) for s in expected])


def test_power_set_size():
    nums = [1, 2, 3, 4]
    result = subsets(nums)
    assert len(result) == 2 ** len(nums)


def test_no_duplicate_subsets():
    result = subsets([1, 2, 3])
    as_tuples = [tuple(sorted(s)) for s in result]
    assert len(as_tuples) == len(set(as_tuples))
