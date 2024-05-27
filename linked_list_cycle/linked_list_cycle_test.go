package linkedlistcycle

import "testing"

func TestHasCycle(t *testing.T) {
	one := NewListNode(1)
	two := NewListNode(2)
	one.Next = two
	two.Next = one

	if result := hasCycle(one); !result {
		t.Errorf("Expected %v, got %v", true, result)
	}
}