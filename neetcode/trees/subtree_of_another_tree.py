def isSubTree(root, subRoot):
    result = False

    def rootTraversal(node):
        if not node:
            return

        # travese
        rootTraversal(node.left)
        rootTraversal(node.right)

        # post
        if subrootTraversal(node, subRoot):
            nonlocal result
            result = True

    rootTraversal(root)

    return result


def subrootTraversal(n, m):
    if not n and not m:
        return True
    elif not n or not m:
        return False
    elif n.val != m.val:
        return False

    l = subrootTraversal(n.left, m.left)
    r = subrootTraversal(n.right, m.right)

    return l and r
