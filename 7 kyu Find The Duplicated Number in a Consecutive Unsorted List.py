def find_dup(arr):
    for i in arr:
        if arr.count(i) == 2:
            return i


print(find_dup([5, 4, 3, 2, 1, 1]), 1)
print(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)