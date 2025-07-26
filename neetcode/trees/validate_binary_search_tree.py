from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    is_valid = True

    def inOrderTraversal(path: List[int], node: TreeNode):
        if not node:
            return

        inOrderTraversal(path, node.left)

        if path and node.val < path[-1]:
            nonlocal is_valid
            is_valid = False

        path.append(node.val)

        inOrderTraversal(path, node.right)

    inOrderTraversal([], root)

    return is_valid
