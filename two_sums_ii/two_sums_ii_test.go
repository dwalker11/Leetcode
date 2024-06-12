package twosumsii

import (
	"slices"
	"testing"
)

var data = []struct {
	name     string
	numbers  []int
	target   int
	expected []int
}{
	{"First", []int{2, 7, 11, 15}, 9, []int{1, 2}},
	{"Second", []int{2, 3, 4}, 6, []int{1, 3}},
	{"Third", []int{-1, 0}, -1, []int{1, 2}},
}

func TestTwoSum(t *testing.T) {
	for _, d := range data {
		t.Run(d.name, func(t *testing.T) {
			if result := twoSum(d.numbers, d.target); slices.Compare(result, d.expected) != 0 {
				t.Errorf("Error: Expected %v got %v", d.expected, result)
			}
		})
	}
}
