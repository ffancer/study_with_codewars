def averages(arr):
    i = 0
    lst = []

    while i < len(arr) - 1:
        lst.append(arr[i] + arr[i + 1])
        i += 1

    return lst


print(averages([2, 2, 2, 2]))
print(averages([0, 0, 0, 0]))
print(averages([2, 4, 3, -4.5]))
print(averages([]))
