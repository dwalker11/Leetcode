def carFleet(target, position, speed):
    count = 0
    cars_sorted_by_position = sorted(range(len(position)), key=lambda i: position[i])

    while cars_sorted_by_position:
        ahead = None
        for curr in reversed(cars_sorted_by_position):
            position[curr] += speed[curr]

            if ahead and position[curr] > position[ahead]:
                position[curr] = position[ahead]
                speed[curr] = speed[ahead]

            ahead = curr

        arrival_time = 0
        while cars_sorted_by_position:
            top = cars_sorted_by_position[-1]

            if not position[top] >= target:
                break
            elif position[top] != arrival_time:
                arrival_time = position[top]
                count += 1

            cars_sorted_by_position.pop()

    print(count)

    return count

carFleet(20, [6,2,17], [3,9,2]) # Expect 2
carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]) # Expect 6
carFleet(10, [0, 4, 2], [2, 1, 3]) # Expect 1
carFleet(10, [3], [3]) # Expect 1
carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) # Expect 3
carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]) # Expect 3
carFleet(10, [1, 4], [3, 2]) # Expect 1