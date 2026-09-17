from solution import TreeNode, invert_tree


def tree_to_list(root):
    """BFS level-order serialization (None for missing nodes, trailing Nones stripped)."""
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
    # Strip trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result


def build_tree(vals):
    """Build tree from level-order list (None for missing nodes)."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while queue and i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


def test_example_case():
    # Tree: [4,2,7,1,3,6,9] -> inverted: [4,7,2,9,6,3,1]
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
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
    # Tree: root=1, left=2, right=None -> inverted: root=1, left=None, right=2
    root = TreeNode(1, left=TreeNode(2))
    result = invert_tree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right is not None
    assert result.right.val == 2


def test_symmetric_tree():
    # Symmetric tree [1,2,2,3,4,4,3] -> inverted [1,2,2,3,4,4,3]
    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    result = invert_tree(root)
    assert tree_to_list(result) == [1, 2, 2, 3, 4, 4, 3]


def test_left_skewed_tree():
    # 1 -> 2 -> 3 (all left children) -> inverted: all right children
    root = TreeNode(1, left=TreeNode(2, left=TreeNode(3)))
    result = invert_tree(root)
    assert result.val == 1
    assert result.left is None
    assert result.right.val == 2
    assert result.right.left is None
    assert result.right.right.val == 3
