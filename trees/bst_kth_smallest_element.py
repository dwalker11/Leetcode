from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    res = -1

    def inOrderTraversal(path, node):
        if not node:
            return

        inOrderTraversal(path, node.left)

        path.append(node.val)

        if k == len(path):
            nonlocal res
            res = path[-1]

        inOrderTraversal(path, node.right)

    inOrderTraversal([], root)

    return res
