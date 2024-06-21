package containerwithmostwater

import "fmt"

func maxArea(height []int) int {
	maxArea := 0

	l := 0
	r := len(height) - 1
	for l < r {
		fmt.Println(l, r)

		// calculate the area
		area := (r - l) * min(height[l], height[r])

		// update maxArea if new area is greater than max
		if area > maxArea {
			maxArea = area
		}

		if height[l] < height[r] {
			l++
		} else {
			r--
		}
	}

	return maxArea
}
