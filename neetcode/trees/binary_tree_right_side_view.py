from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBST(vals):
    if not vals:
        return None

    m = len(vals) // 2
    val = vals[m]

    left = createBST(vals[:m])
    right = createBST(vals[m+1:])
    node = TreeNode(val, left, right)

    return node


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []

    if not root:
        return res

    q = deque()
    q.append(root)

    while q:
        level = []
        size = len(q)

        for _ in range(size):
            node = q.popleft()

            if not node:
                continue

            # process node
            level.append(node.val)

            q.append(node.left)
            q.append(node.right)

        if level:
            res.append(level[-1])

    return res


tree = createBST([4, 2, 5, 1, 6, 3, 7])
