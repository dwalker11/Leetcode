package three_sum

import (
	"fmt"
	"testing"
)

func TestThreeSum(t *testing.T) {
	var result [][]int

	result = threeSum([]int{-1, 0, 1, 2, -1, -4})
	fmt.Println(result)

	result = threeSum([]int{0, 1, 1})
	fmt.Println(result)

	result = threeSum([]int{0, 0, 0})
	fmt.Println(result)
}
