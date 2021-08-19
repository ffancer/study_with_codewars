from math import ceil


def round_to_next5(n):
    return ceil(n / 5) * 5


print(round_to_next5(0))
print(round_to_next5(2))
print(round_to_next5(3))
print(round_to_next5(30))
print(round_to_next5(32))
