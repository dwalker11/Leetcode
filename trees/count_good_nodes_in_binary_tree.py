from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def goodNodes(root: TreeNode) -> int:
    good_nodes = []

    def findGoodNodes(predecessors, node) -> List[int]:
        if not node:
            return

        if not predecessors or node.val >= max(predecessors):
            nonlocal good_nodes
            good_nodes.append(node.val)

        findGoodNodes([*predecessors, node.val], node.left)
        findGoodNodes([*predecessors, node.val], node.right)

    findGoodNodes([], root)

    return len(good_nodes)
