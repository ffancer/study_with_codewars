def elevator_distance(array):
    i, j = 0, 1
    total = 0

    while j < len(array):
        total += abs(array[i] - array[j])
        i += 1
        j += 1

    return total


print(elevator_distance([5, 2, 8]), 9)
print(elevator_distance([1, 2, 3]), 2)
print(elevator_distance([7, 1, 7, 1]), 18)
