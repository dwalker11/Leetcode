package topkfrequentelements

func topKFrequent(nums []int, k int) []int {
	var result []int

	numMap := make(map[int]int)

	for _, num := range nums {
		if _, ok := numMap[num]; !ok {
			numMap[num] = 0
		}

		numMap[num] += 1
	}

	for num, numCount := range numMap {
		if numCount >= k {
			result = append(result, num)
		}
	}

	return result
}
