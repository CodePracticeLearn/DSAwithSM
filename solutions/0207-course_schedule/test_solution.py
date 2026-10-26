from solution import can_finish


def test_example_no_prerequisites():
    assert can_finish(2, []) == True


def test_example_simple_chain():
    assert can_finish(2, [[1, 0]]) == True


def test_example_cycle():
    assert can_finish(2, [[1, 0], [0, 1]]) == False


def test_single_course():
    assert can_finish(1, []) == True


def test_multiple_courses_no_cycle():
    # 0 -> 1 -> 2 -> 3
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) == True


def test_larger_cycle():
    # 0 -> 1 -> 2 -> 0 forms a cycle
    assert can_finish(3, [[1, 0], [2, 1], [0, 2]]) == False


def test_disconnected_graph_no_cycle():
    # Two independent chains: 0->1 and 2->3
    assert can_finish(4, [[1, 0], [3, 2]]) == True


def test_complex_dag():
    # Diamond shape: 0->1, 0->2, 1->3, 2->3
    assert can_finish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True
