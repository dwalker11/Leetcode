def diameterOfBinaryTree(root):
    path = []
    traverse(path, root)
    return len(path) - 1


def traverse(longest_path, node):
    if node is None:
        return []

    left = traverse(longest_path, node.left)
    right = traverse(longest_path, node.right)
    path = [*left, node.val, *right]

    if len(path) > len(longest_path):
        longest_path.clear()
        longest_path.extend(path)

    if len(left) <= len(right):
        return [*right, node.val]

    return [*left, node.val]
