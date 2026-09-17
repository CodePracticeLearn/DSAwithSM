from solution import max_profit

def test_example_case():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5

def test_no_profit():
    assert max_profit([7, 6, 4, 3, 1]) == 0

def test_single_element():
    assert max_profit([5]) == 0

def test_empty_list():
    assert max_profit([]) == 0

def test_all_same_prices():
    assert max_profit([3, 3, 3, 3]) == 0

def test_profit_at_end():
    assert max_profit([2, 4, 1, 7]) == 6
