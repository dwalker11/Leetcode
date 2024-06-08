package longestconsecutivesequence

import (
	"fmt"
	"testing"
)

func TestLongestConsecutive(t *testing.T) {
	var result int

	result = longestConsecutive([]int{100, 4, 200, 1, 3, 2})
	fmt.Println(result)

	result = longestConsecutive([]int{0, 3, 7, 2, 5, 8, 4, 6, 0, 1})
	fmt.Println(result)
}
