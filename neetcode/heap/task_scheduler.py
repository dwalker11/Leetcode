import heapq

from collections import deque
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    lookup = {}

    # Iterate through tasks to create a hash where task -> frequency
    for task in tasks:
        if lookup.get(task) is None:
            lookup[task] = 1
        else:
            lookup[task] += 1

    # Create a priority queue with the task and the frequency of every task
    h = [-freq for freq in lookup.values()]
    heapq.heapify(h)

    q = deque()

    time = 0
    while h or q:
        time += 1

        if h:
            # pop task off of the queue and decrement it's frequency
            count = heapq.heappop(h) + 1

            # add to the queue if count is greater than 0
            if count < 0:
                q.append((count, time + n))

        if q:
            # if the cool-down time is equal to the current time
            count, cooldown_time = q[0]
            if cooldown_time == time:
                # push the task at top of the queue into the heap
                heapq.heappush(h, count)
                q.popleft()

    return time


input = ["B", "C", "D", "A", "A", "A", "A", "G"]
res = leastInterval(input, 1)
print(res)

input = ["A", "C", "A", "B", "D", "B"]
res = leastInterval(input, 1)
print(res)

input = ["A", "A", "A", "B", "B", "B"]
res = leastInterval(input, 2)
print(res)

input = ["A", "A", "A", "B", "B", "B"]
res = leastInterval(input, 3)
print(res)
