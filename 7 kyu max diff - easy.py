def max_diff(lst):
    return 0 if lst == [] else max(lst) - min(lst)


print(max_diff([0, 1, 2, 3, 4, 5, 6]), 6)
print(max_diff([-0, 1, 2, -3, 4, 5, -6]), 11)
print(max_diff([0, 1, 2, 3, 4, 5, 16]), 16)
print(max_diff([16]), 0)
print(max_diff([]), 0)
