from solution import climb_stairs


def test_base_case_one_step():
    assert climb_stairs(1) == 1


def test_base_case_two_steps():
    assert climb_stairs(2) == 2


def test_three_steps():
    assert climb_stairs(3) == 3


def test_four_steps():
    assert climb_stairs(4) == 5


def test_five_steps():
    assert climb_stairs(5) == 8


def test_large_input():
    assert climb_stairs(10) == 89
