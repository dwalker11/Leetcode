from typing import List


def findDuplicate(nums: List[int]) -> int:
    def next(index): return nums[index]

    fast_index = 0
    slow_index = 0

    while True:
        fast_index = next(next(fast_index))
        slow_index = next(slow_index)

        if fast_index == slow_index:
            break

    slow_index = 0

    while True:
        fast_index = next(fast_index)
        slow_index = next(slow_index)

        if fast_index == slow_index:
            break

    return slow_index
