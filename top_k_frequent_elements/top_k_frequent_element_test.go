package topkfrequentelements

import (
	"fmt"
	"slices"
	"testing"
)

func TestTopKFrequent(t *testing.T) {
	var input, result []int

	input = []int{1, 1, 1, 2, 2, 3}
	result = topKFrequent(input, 2)

	if slices.Compare(result, []int{1, 2}) != 0 {
		t.Errorf("Error: results do not match expected output")
		fmt.Println(result)
	}

	input = []int{1}
	result = topKFrequent(input, 1)
	
	if slices.Compare(result, []int{1}) != 0 {
		t.Errorf("Error: results do not match expected output")
		fmt.Println(result)
	}
}
