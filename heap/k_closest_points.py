from heapq import heappop, heappush
import math
from typing import List


def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    res, h = [], []

    # iterate through points adding the distance of each point (to the origin) and their index to a heap
    for i, p in enumerate(points):
        x, y = p[0] - 0, p[1] - 0
        d = math.sqrt(x ** 2 + y ** 2)
        heappush(h, (d, i))

    # pop an element off of the heap and add the point to the results array k times
    for _ in range(k):
        _, i = heappop(h)
        res.append(points[i])

    return res


points = [[1, 3], [-2, 2]]
k = 1
