package longestconsecutivesequence

import (
	"fmt"
	"testing"
)

func TestLongestConsecutive(t *testing.T) {
	var result int

	result = longestConsecutive([]int{100, 4, 200, 1, 3, 2})
	if result != 4 {
		t.Errorf("Error: Expected %d got %d", 4, result)
	}
	fmt.Println(result)

	result = longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1})
	if result != 9 {
		t.Errorf("Error: Expected %d got %d", 9, result)
	}
	fmt.Println(result)
}
