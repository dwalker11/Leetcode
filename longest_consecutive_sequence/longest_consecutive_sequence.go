package longestconsecutivesequence

import (
	"fmt"
	"math"
)

type node struct {
	val  int
	next *node
}

func longestConsecutive(nums []int) int {
	head := &node{}

	for _, v := range nums {
		curr := head
		for curr.next != nil && v > curr.next.val {
			curr = curr.next
		}

		curr.next = &node{val: v, next: curr.next}
	}

	max_consecutive, consecutive := 1, 1

	curr := head.next
	for curr.next != nil {
		if curr.next.val-curr.val == 1 {
			consecutive++
		} else {
			max_consecutive = int(math.Max(float64(max_consecutive), float64(consecutive)))
			consecutive = 0
		}

		curr = curr.next
	}

	fmt.Println()
	max_consecutive = int(math.Max(float64(max_consecutive), float64(consecutive)))

	return max_consecutive
}
