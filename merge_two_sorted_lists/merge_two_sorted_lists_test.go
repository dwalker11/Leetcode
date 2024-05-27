package mergetwosortedlists

import "testing"

func TestMergeTwoLists(t *testing.T) {
	uno := NewListNode(1)
	one := NewListNode(1)
	two := NewListNode(2)
	three := NewListNode(3)
	four := NewListNode(4)
	five := NewListNode(5)
	six := NewListNode(6)

	uno.Next = one
	one.Next = three
	three.Next = five
	two.Next = four
	four.Next = six

	l1 := uno
	l2 := two
	
	printList(l1)
	printList(l2)
	result := mergeTwoLists(l1, l2)
	printList(result)
}