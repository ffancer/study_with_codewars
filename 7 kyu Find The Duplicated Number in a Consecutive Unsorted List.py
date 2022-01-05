def find_dup(arr):
    return len(arr), len(set(arr))
    # if len(arr) == len(set(arr)):
    #     return 'x'


print(find_dup([5, 4, 3, 2, 1, 1]), 1)
print(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)
