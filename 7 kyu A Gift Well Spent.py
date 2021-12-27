def buy(x, arr):
    lst = []
    i, j = 0, 1
    while j < len(arr):
        if arr[i] + arr[j] == x:
            lst.append(i)
            lst.append(j)
        j += 1
        if j == len(arr):
            i += 1
    return lst

print(buy(2, [1, 1]), [0, 1])
# print(buy(3, [1, 1]), None)
print(buy(5, [5, 2, 3, 4, 5]), [1, 2])
# print(buy(5, [1, 2, 3, 4, 5]), [0, 3])
# print(buy(5, [0, 0, 0, 2, 3]), [3, 4])
