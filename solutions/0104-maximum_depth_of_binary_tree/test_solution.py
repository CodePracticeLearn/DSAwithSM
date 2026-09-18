from solution import max_depth


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_example_case():
    # Tree:    3
    #         / \
    #        9  20
    #           / \
    #          15   7
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3


def test_empty_tree():
    assert max_depth(None) == 0


def test_single_node():
    root = TreeNode(1)
    assert max_depth(root) == 1


def test_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert max_depth(root) == 4


def test_right_skewed():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert max_depth(root) == 3


def test_balanced_tree_depth_4():
    root = TreeNode(1,
        TreeNode(2, TreeNode(4, TreeNode(8), TreeNode(9)), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert max_depth(root) == 4
