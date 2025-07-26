def dailyTemperature(temps):
    results = [0 for _ in temps]
    stack = []

    def nextWarmTemp(index):
        while stack:
            top = stack[-1]

            if temps[top] > temps[index]:
                stack.append(index)
                return top - index

            stack.pop()

        stack.append(index)
        return 0

    for index in range(len(temps) - 1, -1, -1):
        results[index] = nextWarmTemp(index)
    
    print(temps)
    print(results)

    return results

dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])
dailyTemperature([30, 40, 50, 60])
dailyTemperature([30, 60, 90])