def average(array):
    return round(sum(array) / len(array))


print(average([5, 78, 52, 900, 1]), 207)
print(average([5, 25, 50, 75]), 39)
print(average([2]), 2)
print(average([1, 1, 1, 1, 9999]), 2001)
print(average([0]), 0)
