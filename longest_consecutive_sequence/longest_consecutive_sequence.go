package longestconsecutivesequence

type set map[int]bool

func longestConsecutive(nums []int) int {
	numSet := make(set)
	for _, v := range nums {
		numSet[v] = true
	}

	maxSequenceLength := 0
	for _, v := range nums {
		if setHasElement(numSet, v-1) {
			continue
		}

		i, sequenceLength := v, 0
		for setHasElement(numSet, i) {
			sequenceLength++
			i++
		}

		if sequenceLength > maxSequenceLength {
			maxSequenceLength = sequenceLength
		}
	}

	return maxSequenceLength
}

func setHasElement(collection set, element int) bool {
	_, ok := collection[element]
	return ok
}
