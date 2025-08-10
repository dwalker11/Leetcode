'''
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.

Constraints:
- 1 <= nums.length <= 104
- 0 <= nums[i] <= 1000
- It's guaranteed that you can reach nums[n - 1].
'''

from typing import List


def jump(nums: List[int]) -> int:
    distances = []
    goal = len(nums) - 1

    for pos in range(goal - 1, -1, -1):
        distance_from_goal = goal - (pos + nums[pos])

        if distance_from_goal < 0:
            distance_from_goal = 0

        # skip until we find the first position that can reach the goal
        if not distances and distance_from_goal != 0:
            continue

        while distances and distance_from_goal <= distances[-1]:
            distances.pop()

        distances.append(distance_from_goal)

    return len(distances)


def main():
    result = jump([2, 3, 1, 1, 4])
    assert result == 2, f"Error: recieved the wrong result: {result}"

    result = jump([2, 3, 0, 1, 4])
    assert result == 2, f"Error: recieved the wrong result: {result}"

    result = jump([1, 2, 1, 1, 1])
    assert result == 3, f"Error: recieved the wrong result: {result}"


if __name__ == "__main__":
    main()
