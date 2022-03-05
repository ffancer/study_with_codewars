from math import ceil, log


def largest_power(N):
    return ceil(log(N, 3)) - 1


print(largest_power(3), 0)
print(largest_power(4), 1)
