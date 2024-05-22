package binarysearch

import "testing"

func TestSearch(t *testing.T) {
	var result int
	var nums = []int{-1, 0, 3, 5, 9, 12}

	if result = search(nums, 9); result != 4 {
		t.Errorf("Expeceted %v, got %v", 4, result)
	}

	if result = search(nums, 2); result != -1 {
		t.Errorf("Expeceted %v, got %v", -1, result)
	}
}
