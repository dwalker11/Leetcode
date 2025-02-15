import math


def minEatingSpeed(piles, h):
    min_k = 0
    l, r = 1, max(piles)

    while l <= r:
        mid = (l + r) // 2
        d = sum([math.ceil(p/mid) for p in piles])

        if d <= h:
            min_k = mid
            r = mid - 1
        elif d > h:
            l = mid + 1

    return min_k


result = minEatingSpeed([1, 4, 3, 2], 9)
print("Expecting: 2, Result:", result)

result = minEatingSpeed([25, 10, 23, 4], 4)
print("Expecting: 25, Result:", result)

# Notes:
# The critical issue is "How can we pick the lowest k that is under h"
