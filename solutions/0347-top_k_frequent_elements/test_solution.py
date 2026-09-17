from solution import top_k_frequent


def test_example_case():
    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]


def test_single_element():
    result = top_k_frequent([1], 1)
    assert result == [1]


def test_all_same_frequency():
    result = top_k_frequent([1, 2, 3], 3)
    assert sorted(result) == [1, 2, 3]


def test_k_equals_one():
    result = top_k_frequent([4, 4, 4, 1, 1, 2, 2, 2, 2], 1)
    assert result == [2]


def test_negative_numbers():
    result = top_k_frequent([-1, -1, -1, 2, 2, 3], 2)
    assert sorted(result) == [-1, 2]


def test_large_k_equals_unique_count():
    result = top_k_frequent([5, 5, 3, 3, 3, 1], 3)
    assert sorted(result) == [1, 3, 5]
