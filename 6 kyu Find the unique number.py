from collections import Counter


def find_uniq(arr):
    return next(i for i in arr if Counter(arr)[i] == 1)





print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
print(find_uniq([10, 3, 3, 3]), 10)
