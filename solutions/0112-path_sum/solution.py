def has_path_sum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == targetSum
    return (has_path_sum(root.left, targetSum - root.val) or
            has_path_sum(root.right, targetSum - root.val))
