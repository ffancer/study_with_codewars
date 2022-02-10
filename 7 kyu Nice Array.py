def is_nice(arr):
    return all(i+1 in arr or i-1 in arr for i in arr)


print(is_nice([2, 10, 9, 3]), True)
print(is_nice([3, 4, 5, 7]), False)
