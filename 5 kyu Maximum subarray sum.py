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
    mininmum = 0
    total = 0
    ans = 0
    for i in range(len(arr)):
        total += arr[i]
        mininmum = min(total, mininmum)
        ans = max(ans, total - mininmum)
    return ans



print(max_sequence([]), 0)
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
