from solution import is_valid

def test_valid_simple_parentheses():
    assert is_valid("()") == True

def test_valid_multiple_types():
    assert is_valid("()[]{}") == True

def test_invalid_mismatched():
    assert is_valid("(]") == False

def test_invalid_wrong_order():
    assert is_valid("([)]") == False

def test_valid_nested():
    assert is_valid("{[]}") == True

def test_empty_string():
    assert is_valid("") == True

def test_single_open_bracket():
    assert is_valid("(") == False

def test_single_close_bracket():
    assert is_valid(")") == False

def test_complex_valid():
    assert is_valid("({[]})[]{}") == True

def test_extra_closing():
    assert is_valid("())") == False
