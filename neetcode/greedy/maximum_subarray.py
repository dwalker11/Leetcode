from typing import List


def maxSubArray(nums: List[int]) -> int:
    max_sum = nums[0]
    new_sum = 0

    for n in nums:
        if new_sum < 0:
            new_sum = 0

        new_sum += n

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

    result = maxSubArray([8, -19, 5, -4, 20])
    print(result)

    result = maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4])
    print(result)


if __name__ == "__main__":
    main()
