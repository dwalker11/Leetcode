package linkedlistcycle

type ListNode struct {
	Val int
	Next *ListNode
}

func NewListNode(val int) *ListNode {
	return &ListNode{Val: val}
}

func hasCycle(head *ListNode) bool {
	var fast, slow *ListNode
	fast = head
	slow = head

	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		
		if fast == slow {
			return true
		}
	}

	return false
}
