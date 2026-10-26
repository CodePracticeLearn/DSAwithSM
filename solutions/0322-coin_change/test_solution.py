from solution import coin_change


def test_example_basic():
    assert coin_change([1, 5, 10, 25], 30) == 2  # 25 + 5


def test_standard_case():
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1


def test_amount_zero():
    assert coin_change([1, 2, 5], 0) == 0


def test_impossible():
    assert coin_change([2], 3) == -1


def test_single_coin():
    assert coin_change([1], 7) == 7


def test_large_amount():
    assert coin_change([1, 5, 10, 25], 100) == 4  # 4 x 25
