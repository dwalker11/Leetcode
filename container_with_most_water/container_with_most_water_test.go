package containerwithmostwater

import "testing"

func TestMaxArea(t *testing.T) {
	var input []int

	input = []int{1, 8, 6, 2, 5, 4, 8, 3, 7}
	if result := maxArea(input); result != 49 {
		t.Errorf("Error: Expected %v got %v", 49, result)
	}

	input = []int{1, 1}
	if result := maxArea(input); result != 1 {
		t.Errorf("Error: Expected %v got %v", 1, result)
	}

	input = []int{2, 3, 4, 5, 18, 17, 6}
	if result := maxArea(input); result != 17 {
		t.Errorf("Error: Expected %v got %v", 17, result)
	}
}
