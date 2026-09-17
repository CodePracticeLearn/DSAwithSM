from solution import max_vowels


def test_example_abciiidef():
    assert max_vowels("abciiidef", 3) == 3


def test_example_aeiou():
    assert max_vowels("aeiou", 2) == 2


def test_example_leetcode():
    assert max_vowels("leetcode", 3) == 2


def test_no_vowels():
    assert max_vowels("bcdfg", 2) == 0


def test_all_vowels():
    assert max_vowels("aeiou", 5) == 5


def test_k_equals_length():
    assert max_vowels("abc", 3) == 1


def test_single_character_vowel():
    assert max_vowels("a", 1) == 1


def test_single_character_consonant():
    assert max_vowels("b", 1) == 0
