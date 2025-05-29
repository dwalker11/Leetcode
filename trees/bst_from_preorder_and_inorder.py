from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    i = -1

    def buildNode(l):
        nonlocal i
        i += 1

        if i == len(preorder):
            return None

        val = preorder[i]
        node = TreeNode(val)

        j = l.index(val)
        left, right = l[:j], l[j+1:]

        if left:
            node.left = buildNode(left)

        if right:
            node.right = buildNode(right)

        return node

    return buildNode(inorder)
