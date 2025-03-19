from typing import Optional


class ListNode:
    def __init__(self, value: int):
        self.val = value
        self.next = None


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    stack = []

    curr = head
    while curr != None:
        stack.append(curr)
        curr = curr.next

    curr = head
    while curr != None:
        node = stack.pop()
        next = curr.next

        if node == next or node == curr:
            break

        curr.next = node
        node.next = next

        top_node = stack[-1]
        top_node.next = None

        curr = next
