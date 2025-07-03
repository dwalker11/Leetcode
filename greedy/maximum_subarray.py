from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = sum(nums)

    i, j = 0, len(nums) - 1
    while i != j:
        if (nums[i] < nums[j]):
            i += 1
        else:
            j -= 1

        new_sum = sum(nums[i:j+1])

        if new_sum > max_sum:
            max_sum = new_sum

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
