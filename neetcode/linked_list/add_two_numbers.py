class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    result = head = ListNode(0)
    carry = 0

    while l1 and l2:
        val, carry = calculate(l1.val, l2.val, carry)

        result.next = ListNode(val)
        result = result.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        val, carry = calculate(l1.val, 0, carry)

        result.next = ListNode(val)
        result = result.next
        l1 = l1.next

    while l2:
        val, carry = calculate(0, l2.val, carry)

        result.next = ListNode(val)
        result = result.next
        l2 = l2.next

    if carry > 0:
        result.next = ListNode(carry)
        result = result.next

    return head.next


def calculate(x, y, carry):
    sum = x + y + carry
    d = sum // 10

    if d == 0:
        return sum, 0

    return sum % 10, d
