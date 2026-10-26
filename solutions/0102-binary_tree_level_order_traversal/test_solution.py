from solution import level_order

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
    assert level_order(root) == [[3], [9, 20], [15, 7]]

def test_empty_tree():
    assert level_order(None) == []

def test_single_node():
    root = TreeNode(42)
    assert level_order(root) == [[42]]

def test_left_skewed():
    root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert level_order(root) == [[1], [2], [3], [4]]

def test_right_skewed():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert level_order(root) == [[1], [2], [3], [4]]

def test_complete_tree():
    #        1
    #       / \
    #      2   3
    #     / \ / \
    #    4  5 6  7
    root = TreeNode(1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7))
    )
    assert level_order(root) == [[1], [2, 3], [4, 5, 6, 7]]
