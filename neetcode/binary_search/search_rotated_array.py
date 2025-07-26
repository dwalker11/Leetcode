def search(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2

        if nums[m] == target:
            return m

        # We are on the left-side
        if nums[m] >= nums[l] and nums[l] > nums[r]:
            if target < nums[l] or target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        # We are on the right-side
        else:
            if target > nums[r] or target < nums[m]:
                r = m - 1
            else:
                l = m + 1

    return -1


results = search([4, 5, 6, 7, 0, 1, 2], 0)
print(f"Expect 4 found: {results}")

results = search([6, 7, 0, 1, 2, 4, 5], 0)
print(f"Expect 2 found: {results}")

results = search([1, 3], 3)
print(f"Expect 1 found: {results}")
