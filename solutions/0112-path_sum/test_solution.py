from solution import has_path_sum


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_example_case():
    # Tree:       5
    #            / \
    #           4   8
    #          /   / \
    #         11  13  4
    #        / \       \
    #       7   2       1
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.right = TreeNode(1)
    # Path: 5->4->11->2 = 22
    assert has_path_sum(root, 22) is True


def test_empty_tree():
    assert has_path_sum(None, 0) is False


def test_single_node_match():
    root = TreeNode(5)
    assert has_path_sum(root, 5) is True


def test_single_node_no_match():
    root = TreeNode(5)
    assert has_path_sum(root, 3) is False


def test_no_matching_path():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert has_path_sum(root, 10) is False


def test_negative_values():
    # Tree:    -2
    #            \
    #            -3
    root = TreeNode(-2)
    root.right = TreeNode(-3)
    assert has_path_sum(root, -5) is True
    assert has_path_sum(root, -2) is False
