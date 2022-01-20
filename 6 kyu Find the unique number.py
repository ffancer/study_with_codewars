def find_uniq(arr):
    n = arr[0]
    for i in arr:
        if i != n:
            return i


print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
