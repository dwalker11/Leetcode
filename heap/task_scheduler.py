from typing import List
import heapq


def leastInterval(tasks: List[str], n: int) -> int:
    lookup = {}

    # Iterate through tasks to create a hash where task -> frequency
    for task in tasks:
        if lookup.get(task) is None:
            lookup[task] = 1
        else:
            lookup[task] += 1

    h = []

    # Create a priority queue with the task and the frequency of every task
    for task in lookup:
        heapq.heappush(h, (-lookup[task], task))

    h2 = []

    i, s = 0, set()
    while h:
        # find the next available position
        while i in s:
            i += 1

        frequency, task = heapq.heappop(h)

        j = i
        for _ in range(-frequency):
            heapq.heappush(h2, (j, task))
            s.add(j)
            j += n + 1

    output = []

    i = 0
    while h2:
        p, task = h2[0]

        if p > i:
            output.append("idle")
        else:
            output.append(task)
            heapq.heappop(h2)

        i += 1

    print(output)

    return len(output)


input = ["B", "C", "D", "A", "A", "A", "A", "G"]
leastInterval(input, 1)

input = ["A", "C", "A", "B", "D", "B"]
leastInterval(input, 1)

input = ["A", "A", "A", "B", "B", "B"]
leastInterval(input, 2)

input = ["A", "A", "A", "B", "B", "B"]
leastInterval(input, 3)
