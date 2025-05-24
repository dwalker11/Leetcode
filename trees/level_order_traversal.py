from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    result = [[]]

    queue = deque()
    queue.append(root)

    count = len(queue)

    while queue:
        node = queue.popleft()
        count -= 1

        if node:
            l = result[-1]
            l.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

        if count < 1:
            count = len(queue)
            result.append([])

    if not result[-1]:
        result.pop()

    return result


def createBST(vals):
    if not vals:
        return None

    m = len(vals) // 2
    val = vals[m]

    left = createBST(vals[:m])
    right = createBST(vals[m+1:])
    node = TreeNode(val, left, right)

    return node


input = createBST([4, 2, 5, 1, 6, 3, 7])
