def averages(arr):
    try:
        lst = []
        for i in range(len(arr) - 1):
            lst.append((arr[i] + arr[i + 1]) / 2)
        return lst
    except:
        return []


print(averages([2, 2, 2, 2]))
print(averages([0, 0, 0, 0]))
print(averages([2, 4, 3, -4.5]))
print(averages([]))
