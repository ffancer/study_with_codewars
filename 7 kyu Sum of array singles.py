def repeats(arr):
    i = 0
    j = i + 1
    lst = []
    while j < len(arr):
        if arr[i] == arr[j]:
            del arr[i]
            del arr[j]
            i += 1
        else:
            j += 1
    return sum(arr)


print(repeats([4, 5, 7, 5, 4, 8]), 15)
print(repeats([9, 10, 19, 13, 19, 13]), 19)
print(repeats([16, 0, 11, 4, 8, 16, 0, 11]), 12)
print(repeats([5, 17, 18, 11, 13, 18, 11, 13]), 22)
print(repeats([5, 10, 19, 13, 10, 13]), 24)
