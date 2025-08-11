'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Constraints:
_
2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''

from functools import cache
from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    @cache
    def dp(i):
        if i >= len(cost):
            return 0
        return cost[i] + min(dp(i + 1), dp(i + 2))

    return min(dp(0), dp(1))


def main():
    result = minCostClimbingStairs([10, 15, 20])
    assert result == 15, f"Error: recieved the wrong result: {result}"

    result = minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
    assert result == 6, f"Error: recieved the wrong result: {result}"


if __name__ == "__main__":
    main()
