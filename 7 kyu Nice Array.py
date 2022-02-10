def is_nice(arr):
    return all(i+1 or i-1 for i in arr)


print(is_nice([2, 10, 9, 3]), True)
print(is_nice([3, 4, 5, 7]), False)
