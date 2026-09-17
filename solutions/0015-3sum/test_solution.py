from solution import three_sum


def test_example_case():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])


def test_no_triplets():
    assert three_sum([1, 2, 3]) == []


def test_all_zeros():
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]


def test_empty_and_short():
    assert three_sum([]) == []
    assert three_sum([0]) == []
    assert three_sum([0, 0]) == []


def test_multiple_duplicates():
    result = three_sum([0, 0, 0, 0])
    assert result == [[0, 0, 0]]


def test_mixed_positives_negatives():
    result = three_sum([-2, 0, 1, 1, 2])
    expected = [[-2, 0, 2], [-2, 1, 1]]
    assert sorted([sorted(t) for t in result]) == sorted([sorted(t) for t in expected])
