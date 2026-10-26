from solution import lowest_common_ancestor


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_example_tree():
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)
    n6 = TreeNode(6, n2, n8)
    return n6, n0, n2, n3, n4, n5, n7, n8, n9


def test_example_lca_2_and_8():
    root, n0, n2, n3, n4, n5, n7, n8, n9 = build_example_tree()
    result = lowest_common_ancestor(root, n2, n8)
    assert result.val == 6


def test_example_lca_2_and_4():
    root, n0, n2, n3, n4, n5, n7, n8, n9 = build_example_tree()
    result = lowest_common_ancestor(root, n2, n4)
    assert result.val == 2


def test_lca_0_and_5():
    root, n0, n2, n3, n4, n5, n7, n8, n9 = build_example_tree()
    result = lowest_common_ancestor(root, n0, n5)
    assert result.val == 2


def test_lca_7_and_9():
    root, n0, n2, n3, n4, n5, n7, n8, n9 = build_example_tree()
    result = lowest_common_ancestor(root, n7, n9)
    assert result.val == 8


def test_node_is_its_own_ancestor():
    root, n0, n2, n3, n4, n5, n7, n8, n9 = build_example_tree()
    result = lowest_common_ancestor(root, root, n2)
    assert result.val == 6


def test_single_node_tree():
    node = TreeNode(1)
    result = lowest_common_ancestor(node, node, node)
    assert result.val == 1
