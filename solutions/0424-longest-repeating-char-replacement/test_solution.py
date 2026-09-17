from solution import character_replacement


def test_example_aababba():
    assert character_replacement("AABABBA", 1) == 4


def test_example_abab():
    assert character_replacement("ABAB", 2) == 4


def test_empty_string():
    assert character_replacement("", 0) == 0


def test_single_character():
    assert character_replacement("A", 0) == 1


def test_all_same_characters():
    assert character_replacement("AAAA", 2) == 4


def test_k_zero_mixed():
    assert character_replacement("ABCDE", 0) == 1


def test_k_larger_than_string():
    assert character_replacement("ABCD", 10) == 4


def test_long_repeating_with_one_diff():
    assert character_replacement("AABAA", 1) == 5
