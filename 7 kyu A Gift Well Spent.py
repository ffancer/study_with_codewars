def buy(x, arr):
    i, j = 0,1

    while i < len(arr):
        if arr[i] + arr[j]==x:
            return [i, j]



print(buy(2, [1, 1]), [0, 1])
print(buy(3, [1, 1]), None)
print(buy(5, [5, 2, 3, 4, 5]), [1, 2])
print(buy(5, [1, 2, 3, 4, 5]), [0, 3])
print(buy(5, [0, 0, 0, 2, 3]), [3, 4])