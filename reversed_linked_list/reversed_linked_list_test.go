package reversedlinkedlist

import "testing"

func TestReversedList(t *testing.T) {
	one := NewNode(1)
	two := NewNode(2)
	three := NewNode(3)
	head := one

	one.Next = two
	two.Next = three
	printList(head)

	reverseedHead := reversedList(head)
	if reverseedHead != three {
		t.Errorf("Expected %v, got %v", three, reverseedHead)
	}

	printList(reverseedHead)
}
