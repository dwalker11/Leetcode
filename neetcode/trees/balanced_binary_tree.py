def isBalanced(root):
    result = True

    def dfs(node):
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        nonlocal result

        if abs(right - left) > 1:
            result = False

        return max(left, right) + 1

    dfs(root)

    return result
