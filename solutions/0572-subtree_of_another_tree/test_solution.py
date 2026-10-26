from solution import is_subtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def test_example1():
    # root = [3,4,5,1,2], subRoot = [4,1,2]
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root, subRoot) == True

def test_example2():
    # root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2]
    root = TreeNode(3,
        TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None)),
        TreeNode(5))
    subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root, subRoot) == False

def test_single_node_match():
    root = TreeNode(1)
    subRoot = TreeNode(1)
    assert is_subtree(root, subRoot) == True

def test_single_node_no_match():
    root = TreeNode(1)
    subRoot = TreeNode(2)
    assert is_subtree(root, subRoot) == False

def test_subroot_is_leaf():
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    subRoot = TreeNode(3)
    assert is_subtree(root, subRoot) == True

def test_root_none():
    assert is_subtree(None, TreeNode(1)) == False
