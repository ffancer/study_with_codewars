# 8 kyu
# Training JS #32: methods of Math---round() ceil() and floor()
from math import ceil, floor


def round_it(n):
    lst = str(n).split('.')

    if len(lst[1]) > len(lst[0]):
        return ceil(n)
    elif len(lst[0]) > len(lst[1]):
        return floor(n)
    return round(n)

print(round_it(3.45), 4)
print(round_it(34.5), 34)
print(round_it(34.56), 35)
