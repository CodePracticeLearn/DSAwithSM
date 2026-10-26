from solution import Node, clone_graph


def test_none_input():
    assert clone_graph(None) is None


def test_single_node():
    node = Node(1)
    cloned = clone_graph(node)
    assert cloned is not node
    assert cloned.val == 1
    assert cloned.neighbors == []


def test_two_nodes():
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    c1 = clone_graph(n1)
    assert c1 is not n1
    assert c1.val == 1
    assert len(c1.neighbors) == 1
    c2 = c1.neighbors[0]
    assert c2 is not n2
    assert c2.val == 2
    assert len(c2.neighbors) == 1
    assert c2.neighbors[0] is c1


def test_example_four_nodes():
    # Graph: 1--2, 1--4, 2--3, 3--4
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    c1 = clone_graph(n1)

    # BFS to collect all cloned nodes
    visited = {}
    queue = [c1]
    visited[c1.val] = c1
    while queue:
        cur = queue.pop(0)
        for nb in cur.neighbors:
            if nb.val not in visited:
                visited[nb.val] = nb
                queue.append(nb)

    assert len(visited) == 4
    for val in [1, 2, 3, 4]:
        assert val in visited

    # Ensure deep copy (no original nodes present)
    originals = {id(n1), id(n2), id(n3), id(n4)}
    for v in visited.values():
        assert id(v) not in originals

    # Check neighbor structure
    assert sorted([nb.val for nb in visited[1].neighbors]) == [2, 4]
    assert sorted([nb.val for nb in visited[2].neighbors]) == [1, 3]
    assert sorted([nb.val for nb in visited[3].neighbors]) == [2, 4]
    assert sorted([nb.val for nb in visited[4].neighbors]) == [1, 3]


def test_self_loop():
    n1 = Node(1)
    n1.neighbors = [n1]
    c1 = clone_graph(n1)
    assert c1 is not n1
    assert c1.val == 1
    assert len(c1.neighbors) == 1
    assert c1.neighbors[0] is c1


def test_triangle():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2, n3]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n1, n2]

    c1 = clone_graph(n1)
    assert c1 is not n1
    assert c1.val == 1
    nb_vals = sorted([nb.val for nb in c1.neighbors])
    assert nb_vals == [2, 3]
    # Verify the clone of node 2 points back to c1
    c2 = [nb for nb in c1.neighbors if nb.val == 2][0]
    assert c1 in c2.neighbors
