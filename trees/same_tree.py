def isSameTree(p, q):
    if not p and not q:
        return True
    elif not p or not q:
        return False

    result = p.val == q.val
    result_l = isSameTree(p.left, q.left)
    result_r = isSameTree(p.right, q.right)

    return result and result_l and result_r
