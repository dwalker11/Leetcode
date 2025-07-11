from typing import List


def canJump(nums: List[int]) -> bool:
    if len(nums) == 1:
        return True

    start, end = 0, len(nums) - 1

    curr = start
    max_jump_distance = nums[curr]

    while True:
        if max_jump_distance == 0:
            break

        new_position = curr + max_jump_distance

        if new_position >= end:
            return True

        curr = new_position
        max_jump_distance = nums[curr]

    return False


def main():
    result = canJump([2, 3, 1, 1, 4])
    print(result)

    result = canJump([3, 2, 1, 0, 4])
    print(result)


if __name__ == "__main__":
    main()
