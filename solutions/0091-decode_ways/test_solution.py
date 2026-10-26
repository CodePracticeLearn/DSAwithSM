from solution import num_decodings

def test_example_12():
    assert num_decodings("12") == 2  # "AB" or "L"

def test_example_226():
    assert num_decodings("226") == 3  # "BZ", "VF", "BBF"

def test_single_digit():
    assert num_decodings("1") == 1
    assert num_decodings("9") == 1

def test_leading_zero():
    assert num_decodings("0") == 0
    assert num_decodings("06") == 0

def test_contains_zero():
    assert num_decodings("10") == 1
    assert num_decodings("20") == 1
    assert num_decodings("30") == 0
    assert num_decodings("100") == 0
    assert num_decodings("1020") == 1

def test_longer_string():
    assert num_decodings("11106") == 2
    assert num_decodings("111") == 3  # "AAA", "KA", "AK"
    assert num_decodings("27") == 1  # only "BG", since 27 > 26

def test_all_ones():
    # Fibonacci-like growth: "1111" -> 5 ways
    assert num_decodings("1111") == 5
