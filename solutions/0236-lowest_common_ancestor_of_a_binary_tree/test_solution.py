from solution import lowest_common_ancestor


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_example_case():
    #        3
    #       / \
    #      5   1
    #     / \ / \
    #    6  2 0  8
    #      / \
    #     7   4
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node2 = TreeNode(2, node7, node4)
    node0 = TreeNode(0)
    node8 = TreeNode(8)
    node5 = TreeNode(5, node6, node2)
    node1 = TreeNode(1, node0, node8)
    root = TreeNode(3, node5, node1)

    assert lowest_common_ancestor(root, node5, node1) == root
    assert lowest_common_ancestor(root, node5, node4) == node5


def test_lca_is_one_of_the_nodes():
    #    1
    #   /
    #  2
    node2 = TreeNode(2)
    root = TreeNode(1, node2, None)
    assert lowest_common_ancestor(root, root, node2) == root


def test_single_node_tree():
    root = TreeNode(1)
    assert lowest_common_ancestor(root, root, root) == root


def test_deep_left_and_right():
    #        1
    #       / \
    #      2   3
    #     /     \
    #    4       5
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, None)
    node3 = TreeNode(3, None, node5)
    root = TreeNode(1, node2, node3)

    assert lowest_common_ancestor(root, node4, node5) == root
    assert lowest_common_ancestor(root, node4, node2) == node2
    assert lowest_common_ancestor(root, node3, node5) == node3


def test_both_on_same_side():
    #      1
    #     /
    #    2
    #   / \
    #  3   4
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node2 = TreeNode(2, node3, node4)
    root = TreeNode(1, node2, None)

    assert lowest_common_ancestor(root, node3, node4) == node2


def test_p_equals_q():
    node2 = TreeNode(2)
    root = TreeNode(1, node2, None)
    assert lowest_common_ancestor(root, node2, node2) == node2
