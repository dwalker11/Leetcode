from typing import List
import heapq


def lastStoneWeight(stones: List[int]) -> int:
    h = [-s for s in stones]

    heapq.heapify(h)

    while len(h) > 1:
        y = -heapq.heappop(h)
        x = -heapq.heappop(h)

        if x != y:
            res = y - x
            heapq.heappush(h, -res)

    if not h:
        return 0

    return -h[0]


result = lastStoneWeight([2, 7, 4, 1, 8, 1])
print(result)
