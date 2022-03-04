import itertools

def catch_sign_change(lst):
    return max(sum(1 for key in itertools.groupby(lst, lambda x: x >= 0)) - 1, 0)




print(catch_sign_change([1, 3, 4, 5]), 0)
print(catch_sign_change([1, -3, -4, 0, 5]), 2)
print(catch_sign_change([]), 0)
print(catch_sign_change([-47, 84, -30, -11, -5, 74, 77]), 3)
