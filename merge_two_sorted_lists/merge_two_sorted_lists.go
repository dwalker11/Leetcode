package mergetwosortedlists

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func NewListNode(val int) *ListNode {
	return &ListNode{Val: val}
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var head, curr *ListNode

	if list1 == nil {
		return list2
	}

	if list2 == nil {
		return list1
	}

	if list1.Val <= list2.Val {
		head = list1
		list1 = list1.Next
	} else {
		head = list2
		list2 = list2.Next
	}

	curr = head

	for list1 != nil || list2 != nil {
		switch {
		case list1 == nil:
			curr.Next = list2
			curr = list2
			list2 = list2.Next
		case list2 == nil:
			curr.Next = list1
			curr = list1
			list1 = list1.Next
		case list1.Val <= list2.Val:
			curr.Next = list1
			curr = list1
			list1 = list1.Next
		case list2.Val < list1.Val:
			curr.Next = list2
			curr = list2
			list2 = list2.Next
		}
	}

	return head
}

func printList(head *ListNode) {
	curr := head
	for curr != nil {
		fmt.Printf("%v ", curr.Val)
		curr = curr.Next
	}
	fmt.Println()
}
