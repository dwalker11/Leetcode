package productofarrayexceptself

import (
	"fmt"
	"slices"
	"testing"
)

func TestProductExceptSelf(t *testing.T) {
	var output []int

	output = productExceptSelf([]int{1, 2, 3, 4})
	fmt.Println(output)

	if result := slices.Compare(output, []int{24, 12, 8, 6}); result != 0 {
		t.Errorf("Error: The result does not match the expected output.")
	}

	output = productExceptSelf([]int{-1, 1, 0, -3, 3})
	fmt.Println(output)

	if result := slices.Compare(output, []int{0, 0, 9, 0, 0}); result != 0 {
		t.Errorf("Error: The result does not match the expected output.")
	}
}
