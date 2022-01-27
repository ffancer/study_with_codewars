def max_sequence(arr):
    # if not arr:
    #     return 0
    # if all(i for i in arr) > 0:
    #     return sum(arr)
    # if all(i for i in arr) < 0:
    #     return 0

    # sum_1 = 0
    # sum_2 = 0
    # lst = []
    #
    # for i in arr:
    lst = []
    total = 0
    maximum = 0
    for i in range(len(arr)):
        total += arr[i]
        lst.append(arr[i])
        if total < 0:
            total = 0
            lst = []
        if total > 0:
            maximum = total
    return maximum



print(max_sequence([]), 0)
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
