def findMin(nums):
    if nums[0] <= nums[-1]:
        return nums[0]

    while nums:
        mid = len(nums) // 2
        first_half, second_half = nums[:mid], nums[mid:]

        if first_half[-1] > second_half[0]:
            return second_half[0]
        elif len(first_half) > 1 and first_half[0] > first_half[-1]:
            nums = first_half
        elif len(second_half) > 1 and second_half[0] > second_half[-1]:
            nums = second_half


results = findMin([1, 2, 3, 4, 5, 6])
print(f"Expect: 1 found: {results}")

results = findMin([5, 6, 1, 2, 3, 4])
print(f"Expect: 1 found: {results}")
