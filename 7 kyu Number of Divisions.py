from math import log


def divisions(n, divisor):
    return int(log(n, divisor))


print(divisions(6, 2), 2)
print(divisions(100, 2), 6)
print(divisions(2450, 5), 4)
print(divisions(9999, 3), 8)
print(divisions(2, 3), 0)
print(divisions(5, 5), 1)
