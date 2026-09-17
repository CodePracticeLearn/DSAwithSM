from solution import length_of_longest_substring

def test_example_abcabcbb():
    assert length_of_longest_substring("abcabcbb") == 3

def test_example_bbbbb():
    assert length_of_longest_substring("bbbbb") == 1

def test_example_pwwkew():
    assert length_of_longest_substring("pwwkew") == 3

def test_empty_string():
    assert length_of_longest_substring("") == 0

def test_single_character():
    assert length_of_longest_substring("a") == 1

def test_all_unique():
    assert length_of_longest_substring("abcdef") == 6

def test_repeating_at_edges():
    assert length_of_longest_substring("abcda") == 4
