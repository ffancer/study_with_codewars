def min_sum(arr):
    mx = max(arr)
    mn = min(arr)
    total = 0

    while len(arr):
        total += mn * mx
        arr.remove(mn)
        arr.remove(mx)
        if not arr:
            return total
        mx = max(arr)
        mn = min(arr)

    return total


print(min_sum([5, 4, 2, 3]), 22)
print(min_sum([12, 6, 10, 26, 3, 24]), 342)
print(min_sum([9, 2, 8, 7, 5, 4, 0, 6]), 74)
