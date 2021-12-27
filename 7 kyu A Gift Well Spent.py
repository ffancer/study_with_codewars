def buy(x, arr):
    if len(arr) < 2 or sum(arr) < x:
        return None
    for i in range(len(arr)):
        # print(i, arr[i])
        for j in range(len(arr)):
            print(j, arr[j])



print(buy(0, [2, -2]), [0, 1])
print(buy(2, [1, 1]), [0, 1])
print(buy(3, [1, 1]), None)
print(buy(5, [5, 2, 3, 4, 5]), [1, 2])
print(buy(5, [1, 2, 3, 4, 5]), [0, 3])
print(buy(5, [0, 0, 0, 2, 3]), [3, 4])
