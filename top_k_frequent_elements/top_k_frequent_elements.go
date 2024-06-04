package topkfrequentelements

func topKFrequent(nums []int, k int) []int {
	var result []int

	numMap := make(map[int]int)

	for _, num := range nums {
		numMap[num] += 1
	}

	for i := 0; i < k; i++ {
		var largest int

		for num, count := range numMap {
			if count > numMap[largest] {
				largest = num
			}
		}

		result = append(result, largest)
		delete(numMap, largest)
	}

	return result
}
