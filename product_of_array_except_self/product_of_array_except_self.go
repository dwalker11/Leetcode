package productofarrayexceptself

func productExceptSelf(nums []int) []int {
	result := make([]int, len(nums))

	for i := range result {
		result[i] = 1
	}

	prevProduct := nums[0]

	for i := 1; i < len(nums); i++ {
		result[i] = prevProduct

		for j := i - 1; j >= 0; j-- {
			result[j] *= nums[i]
		}

		prevProduct *= nums[i]
	}

	return result
}
