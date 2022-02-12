def duplicates(arr):
    return sum(arr.count(i)//2 for i in set(arr))


print(duplicates([1, 2, 5, 6, 5, 2]), 2)
print(duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]), 4)
print(duplicates([0, 0, 0, 0, 0, 0, 0]), 3)
print(duplicates([1000, 1000]), 1)
print(duplicates([]), 0)
print(duplicates([54]), 0)
