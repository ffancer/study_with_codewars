def median(array):
    array = sorted(array)
    return array[len(array) // 2] if len(array) % 2 != 0 else (array[len(array) // 2] + array[(len(array) - 1) // 2]) / 2

print(median([3, 2, 1]), 2)
print(median([1]), 1)
print(median([1234, 345, 78]), 345)
print(median([33, 99, 100, 30, 29, 50]), 41.5)
print(median([3, 50]), 26.5)