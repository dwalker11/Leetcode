def maxDepth(root) -> int:
    if root is None:
        return 0
    else:
        return traverse(root)


def traverse(node) -> int:
    if node is None:
        return 0

    return max(traverse(node.left), traverse(node.right)) + 1
