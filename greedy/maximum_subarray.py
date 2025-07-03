from typing import List


def maxSubArray(nums: List[int]) -> int:
    i, j = 0, 1

    max_sum = nums[i]

    while j < len(nums):
        new_sum, val = sum(nums[i:j+1]), nums[j]

        if max_sum <= val and new_sum <= val:
            i, new_sum = j, nums[j]

        if new_sum == max_sum:
            i = j - 1
            while i >= 0 and sum(nums[i:j+1]) != max_sum:
                i -= 1
        elif new_sum > max_sum:
            max_sum = new_sum

        j += 1

    return max_sum


def main():
    result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)

    result = maxSubArray([1])
    print(result)

    result = maxSubArray([5, 4, -1, 7, 8])
    print(result)

    result = maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4])
    print(result)


if __name__ == "__main__":
    main()
