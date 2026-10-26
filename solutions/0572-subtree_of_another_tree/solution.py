def is_subtree(root, subRoot):
    def is_same(p, q):
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return is_same(p.left, q.left) and is_same(p.right, q.right)

    if not root: return False
    if is_same(root, subRoot): return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)
