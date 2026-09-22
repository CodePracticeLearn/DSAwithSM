from solution import diameter_of_binary_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_example_case():
    # Tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    # Diameter is 3 (path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert diameter_of_binary_tree(root) == 3


def test_single_node():
    root = TreeNode(1)
    assert diameter_of_binary_tree(root) == 0


def test_none_root():
    assert diameter_of_binary_tree(None) == 0


def test_two_nodes():
    root = TreeNode(1)
    root.left = TreeNode(2)
    assert diameter_of_binary_tree(root) == 1


def test_diameter_not_through_root():
    # Tree:
    #         1
    #        /
    #       2
    #      / \
    #     3   4
    #    /     \
    #   5       6
    # Diameter is 4 (path: 5 -> 3 -> 2 -> 4 -> 6), does not pass through root
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.right.right = TreeNode(6)
    assert diameter_of_binary_tree(root) == 4


def test_straight_line():
    # Tree: 1 -> 2 -> 3 -> 4 (all left children)
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    assert diameter_of_binary_tree(root) == 3
