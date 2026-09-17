from solution import min_window


def test_example_basic():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"


def test_single_char_match():
    assert min_window("a", "a") == "a"


def test_no_match():
    assert min_window("a", "aa") == ""


def test_empty_inputs():
    assert min_window("", "A") == ""
    assert min_window("A", "") == ""
    assert min_window("", "") == ""


def test_t_equals_s():
    assert min_window("abc", "abc") == "abc"


def test_entire_string_is_minimum():
    assert min_window("ab", "b") == "b"


def test_multiple_occurrences_needed():
    # t requires two 'a's
    result = min_window("adobecodebaaanc", "aaa")
    assert result == "aaa"


def test_all_same_characters():
    assert min_window("aaaa", "aa") == "aa"


def test_no_valid_window():
    assert min_window("abcdef", "z") == ""


def test_window_at_start():
    assert min_window("abcdef", "ab") == "ab"
