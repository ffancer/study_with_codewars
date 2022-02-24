def unique_sum(lst):
    if not lst:
        return None
    return sum(set(lst))


print(unique_sum([1, 2, 3]), 6)
print(unique_sum([1, 3, 8, 1, 8]), 12)
print(unique_sum([-1, -1, 5, 2, -7]), -1)
