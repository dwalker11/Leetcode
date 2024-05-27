package reversedlinkedlist

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

func NewNode(val int) *ListNode {
	return &ListNode{
		Val: val,
	}
}

func reversedList(head *ListNode) *ListNode {
	var prev, curr, next *ListNode

	if head == nil || head.Next == nil {
		return head
	}

	curr = head
	next = head.Next

	for next != nil {
		curr.Next = prev
		prev = curr
		curr = next
		next = next.Next
	}

	curr.Next = prev

	return curr
}

func printList(head *ListNode) {
	curr := head
	for curr != nil {
		fmt.Print(curr.Val)
		curr = curr.Next
	}
}
