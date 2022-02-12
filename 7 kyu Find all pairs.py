def duplicates(arr):
    cnt = 0
    dct = {i: arr.count(i) for i in arr}
    return dct

print(duplicates([1, 2, 5, 6, 5, 2]), 2)
print(duplicates([1, 2, 2, 20, 6, 20, 2, 6, 2]), 4)
print(duplicates([0, 0, 0, 0, 0, 0, 0]), 3)
print(duplicates([1000, 1000]), 1)
print(duplicates([]), 0)
print(duplicates([54]), 0)
