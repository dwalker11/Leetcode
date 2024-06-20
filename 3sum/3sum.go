package three_sum

import "slices"

func threeSum(nums []int) [][]int {
	var results [][]int

	slices.Sort(nums)

	for i := range nums {
		// ...skip if current is equal to previous
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}

		l, r := i+1, len(nums)-1
		for l < r {
			sum := nums[i] + nums[l] + nums[r]

			if sum < 0 {
				l++
			} else if sum > 0 {
				r--
			} else {
				results = append(results, []int{nums[i], nums[l], nums[r]})
				l++

				// while l is not equal to the previous l
				for nums[l] == nums[l - 1] && l < r {
					l++
				}
			}
		}
	}

	return results
}
