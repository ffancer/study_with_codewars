def consecutive(arr, a, b):
    return abs(arr.index(b) - arr.index(a)) == 1


print(consecutive([1, 3, 5, 7], 3, 7), False)
print(consecutive([1, 3, 5, 7], 3, 1), True)
print(consecutive([1, 6, 9, -3, 4, -78, 0], -3, 4), True)