from math import factorial as fac


def am_i_wilson(n):
    return n * fac(n-1)


print(am_i_wilson(0), False)
print(am_i_wilson(1), False)
print(am_i_wilson(5), True)
print(am_i_wilson(8), False)
print(am_i_wilson(9), False)
