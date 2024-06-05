package topkfrequentelements

func topKFrequent(nums []int, k int) []int {
	var result []int

	numMap := make(map[int]int)
	for _, num := range nums {
		numMap[num] += 1
	}

	buckets := make([][]int, len(nums) + 1)
	for num, count := range numMap {
		buckets[count] = append(buckets[count], num)
	}

outer:
	for i := len(buckets) - 1; i >= 0; i-- {
		for _, v := range buckets[i] {
			if len(result) == k {
				break outer
			}

			result = append(result, v)
		}
	}

	return result
}
