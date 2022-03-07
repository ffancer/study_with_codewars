def peak(arr):
    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1:])
        if left_sum == right_sum:
            return i
    return -1


print(peak([1, 2, 3, 5, 3, 2, 1]), 3)
print(peak([1, 12, 3, 3, 6, 3, 1]), 2)
print(peak([10, 20, 30, 40]), -1)
