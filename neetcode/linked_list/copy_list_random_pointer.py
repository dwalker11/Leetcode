class ListNode:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


def create_linked_list():
    head = curr = ListNode(1)

    for i in range(2, 5):
        node = ListNode(i)
        curr.next = node
        curr = node

    return head


def print_list(head: ListNode):
    curr = head
    while curr:
        print(f"[{curr.val} {curr.random}]")
        curr = curr.next


def copyRandomList(head):
    if head is None:
        return None

    source_to_copy_map = {}

    head_copy = copyNode(head)
    source_to_copy_map[head] = head_copy

    main_node = head.next
    copy_node = head_copy

    while main_node:
        node = copyNode(main_node)
        copy_node.next = node
        source_to_copy_map[main_node] = node

        main_node = main_node.next
        copy_node = copy_node.next

    main_node = head
    copy_node = head_copy

    while main_node:
        node = main_node.random

        if node is None:
            copy_node.random = node
        else:
            # use the hash to lookup the copied node of the fetched node
            # set current copy_node to point to node fetched from the hash
            copy_node.random = source_to_copy_map[node]

        main_node = main_node.next
        copy_node = copy_node.next

    return head_copy


def copyNode(node):
    return ListNode(node.val, node.next)
