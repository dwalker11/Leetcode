def dailyTemperature(temps):
    results = []

    def nextWarmTemp(temp, index, count):
        if index == len(temps):
            return 0
        elif temps[index] > temp:
            return count
        else:
            return nextWarmTemp(temp, index + 1, count + 1)

    for index, temp in enumerate(temps):
        num_of_days = nextWarmTemp(temp, index + 1, 1)
        results.append(num_of_days)
    
    print(temps)
    print(results)

    return results

dailyTemperature([73, 74, 75, 71, 69, 72, 76, 73])
dailyTemperature([30, 40, 50, 60])
dailyTemperature([30, 60, 90])