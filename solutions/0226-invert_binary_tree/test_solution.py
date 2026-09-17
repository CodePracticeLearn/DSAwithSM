from solution import TreeNode, invert_tree


def tree_to_list(root):
    """Convert tree to level-order list for easy comparison."""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def test_example_case():
    #       4                4
    #      / \     =>       / \
    #     2   7            7   2
    #    / \ / \          / \ / \
    #   1  3 6  9        9  6 3  1
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(7, TreeNode(6), TreeNode(9))
    )
    result = invert_tree(root)
    assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]


def test_empty_tree():
    assert invert_tree(None) is None


def test_single_node():
    root = TreeNode(1)
    result = invert_tree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right is None


def test_two_levels_left_only():
    #     1          1
    #    /     =>     \
    #   2              2
    root = TreeNode(1, TreeNode(2), None)
    result = invert_tree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right.val == 2


def test_two_levels_both_children():
    #     1          1
    #    / \   =>   / \
    #   2   3      3   2
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = invert_tree(root)
    assert tree_to_list(result) == [1, 3, 2]


def test_asymmetric_tree():
    #       1              1
    #      / \    =>      / \
    #     2   3          3   2
    #      \            /
    #       5          5
    root = TreeNode(1,
        TreeNode(2, None, TreeNode(5)),
        TreeNode(3)
    )
    result = invert_tree(root)
    assert result.val == 1
    assert result.left.val == 3
    assert result.right.val == 2
    assert result.right.left.val == 5
    assert result.right.right is None
    assert result.left.left is None
    assert result.left.right is None
