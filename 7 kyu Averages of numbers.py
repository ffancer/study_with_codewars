def averages(arr):
    i, j = 0, 1
    lst = []

    while j < len(arr):
        lst.append(arr[i] + arr[j])
        i += 1
        j += 1

    return lst


print(averages([2, 2, 2, 2]))
print(averages([0, 0, 0, 0]))
print(averages([2, 4, 3, -4.5]))
print(averages([]))
