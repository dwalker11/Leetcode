from typing import List
import heapq


def findKthLargest(nums: List[int], k: int) -> int:
    heapq.heapify(nums)

    while len(nums) > k:
        heapq.heappop(nums)

    return nums[0]


nums = [3, 2, 1, 5, 6, 4]
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
