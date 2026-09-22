def diameter_of_binary_tree(root):
    result = [0]

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        result[0] = max(result[0], left + right)
        return 1 + max(left, right)

    depth(root)
    return result[0]
