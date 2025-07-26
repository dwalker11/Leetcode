class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
        print(curr.val)
        curr = curr.next


def removeNthFromEnd(head: ListNode, n: int):
    size = 1
    delay_count = n
    curr = pos = head

    while curr.next:
        if delay_count == 0:
            pos = pos.next
        else:
            delay_count -= 1

        curr = curr.next
        size += 1

    if n == size:
        target = head
        head = target.next
    else:
        target = pos.next
        pos.next = target.next

    # target.next = None

    return head


l = create_linked_list()
l2 = removeNthFromEnd(l, 2)
