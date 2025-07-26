from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return root

    invertTree(root.left)
    invertTree(root.right)

    root.left, root.right = root.right, root.left

    return root
