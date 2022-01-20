from collections import Counter


def find_uniq(arr):
    for i, j in Counter(arr).items():
        if j == 1:
            return i


print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
print(find_uniq([10, 3, 3, 3]), 10)
