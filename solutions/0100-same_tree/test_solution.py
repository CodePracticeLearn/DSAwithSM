from solution import is_same_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_same_trees():
    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_different_structure():
    p = TreeNode(1, TreeNode(2), None)
    q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(p, q) is False


def test_different_values():
    p = TreeNode(1, TreeNode(2), TreeNode(1))
    q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(p, q) is False


def test_both_none():
    assert is_same_tree(None, None) is True


def test_one_none():
    p = TreeNode(1)
    assert is_same_tree(p, None) is False
    assert is_same_tree(None, p) is False


def test_single_node_same():
    p = TreeNode(42)
    q = TreeNode(42)
    assert is_same_tree(p, q) is True


def test_deeper_tree():
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert is_same_tree(p, q) is True


def test_deeper_tree_different_leaf():
    p = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    q = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(6)), TreeNode(3))
    assert is_same_tree(p, q) is False
