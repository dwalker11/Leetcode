from typing import List


def canJump(nums: List[int]) -> bool:
    goal = len(nums) - 1

    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i

    return goal == 0


def main():
    result = canJump([2, 3, 1, 1, 4])
    print(result)

    result = canJump([3, 2, 1, 0, 4])
    print(result)


if __name__ == "__main__":
    main()
