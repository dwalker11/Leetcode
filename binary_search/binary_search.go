package binarysearch

import (
	"math"
)

func search(nums []int, target int) int {
	low, high := 0, len(nums)-1

	for low <= high {
		midPoint := int(math.Round(float64(high+low) / 2))
		value := nums[midPoint]

		if target == value {
			return midPoint
		}

		if target < value {
			high = midPoint - 1
		} else if target > value {
			low = midPoint + 1
		}
	}

	return -1
}
