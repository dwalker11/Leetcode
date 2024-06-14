package three_sum

import "slices"

func threeSum(nums []int) [][]int {
	numsMap := make(map[int][]int)
	for i, v := range nums {
		if s, ok := numsMap[v]; !ok {
			numsMap[v] = []int{i}
		} else {
			numsMap[v] = append(s, i)
		}
	}

	solutionSet := make(map[[3]int]bool)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			test := (nums[i] + nums[j]) * -1
			if indicies, ok := numsMap[test]; ok {
				for _, k := range indicies {
					if k == i || k == j {
						continue
					}
					var key [3]int
					s := []int{nums[i], nums[j], nums[k]}
					slices.Sort(s)
					copy(key[:], s)
					solutionSet[key] = true
				}
			}
		}
	}

	var results [][]int
	for k := range solutionSet {
		results = append(results, k[:])
	}

	return results
}
