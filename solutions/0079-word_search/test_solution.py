from solution import exist


def test_example_true():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCCED") == True


def test_example_see():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "SEE") == True


def test_example_false():
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(board, "ABCB") == False


def test_single_cell_match():
    board = [["A"]]
    assert exist(board, "A") == True


def test_single_cell_no_match():
    board = [["A"]]
    assert exist(board, "B") == False


def test_no_reuse():
    # Word requires reusing the same cell, should return False
    board = [["A","B"],["C","D"]]
    assert exist(board, "ABA") == False


def test_snake_path():
    board = [["A","B"],["D","C"]]
    assert exist(board, "ABCD") == True


def test_word_longer_than_grid():
    board = [["A","B"],["C","D"]]
    assert exist(board, "ABCDE") == False
