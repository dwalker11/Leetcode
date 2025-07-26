def lowestCommonAncestor(root, p, q):
    if (p.val <= root <= q.val or q.val <= root <= p.val):
        return root

    if p.val < root:
        return lowestCommonAncestor(root.left, p, q)

    if p.val > root:
        return lowestCommonAncestor(root.right, p, q)
