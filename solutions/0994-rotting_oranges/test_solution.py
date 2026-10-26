from solution import oranges_rotting

def test_example_basic():
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    assert oranges_rotting(grid) == 4

def test_impossible():
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    assert oranges_rotting(grid) == -1

def test_already_no_fresh():
    grid = [[0,2]]
    assert oranges_rotting(grid) == 0

def test_all_empty():
    grid = [[0,0],[0,0]]
    assert oranges_rotting(grid) == 0

def test_single_fresh_adjacent_to_rotten():
    grid = [[2,1]]
    assert oranges_rotting(grid) == 1

def test_single_fresh_no_rotten():
    grid = [[1]]
    assert oranges_rotting(grid) == -1
