def buy(x, arr):
    i = 0
    j = 1
    lst = []
    while True:
        if arr[i] + arr[j] != x:
            j += 1
            if j == len(arr)-1:
                i += 1
        lst.append(i)
        lst.append(j)
    return lst


print(buy(2, [1, 1]), [0, 1])
# print(buy(3, [1, 1]), None)
# print(buy(5, [5, 2, 3, 4, 5]), [1, 2])
# print(buy(5, [1, 2, 3, 4, 5]), [0, 3])
# print(buy(5, [0, 0, 0, 2, 3]), [3, 4])
