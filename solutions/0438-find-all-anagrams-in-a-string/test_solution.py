from solution import find_anagrams


def test_example1():
    assert find_anagrams("cbaebabacd", "abc") == [0, 6]


def test_example2():
    assert find_anagrams("abab", "ab") == [0, 1, 2]


def test_no_match():
    assert find_anagrams("af", "be") == []


def test_p_longer():
    assert find_anagrams("a", "aa") == []
