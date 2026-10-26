from solution import num_islands


def test_example_case():
    grid = [
        ['1', '1', '1', '1', '0'],
        ['1', '1', '0', '1', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '0', '0', '0'],
    ]
    assert num_islands(grid) == 1


def test_multiple_islands():
    grid = [
        ['1', '1', '0', '0', '0'],
        ['1', '1', '0', '0', '0'],
        ['0', '0', '1', '0', '0'],
        ['0', '0', '0', '1', '1'],
    ]
    assert num_islands(grid) == 3


def test_empty_grid():
    assert num_islands([]) == 0


def test_all_water():
    grid = [
        ['0', '0', '0'],
        ['0', '0', '0'],
        ['0', '0', '0'],
    ]
    assert num_islands(grid) == 0


def test_all_land():
    grid = [
        ['1', '1', '1'],
        ['1', '1', '1'],
        ['1', '1', '1'],
    ]
    assert num_islands(grid) == 1


def test_single_cell_island():
    grid = [['1']]
    assert num_islands(grid) == 1


def test_diagonal_not_connected():
    grid = [
        ['1', '0'],
        ['0', '1'],
    ]
    assert num_islands(grid) == 2
