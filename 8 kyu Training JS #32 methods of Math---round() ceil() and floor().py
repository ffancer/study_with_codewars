# 8 kyu
# Training JS #32: methods of Math---round() ceil() and floor()
from math import floor, ceil

def round_it(n):
    l, r = [len(x) for x in str(n).split('.')]
    if r > l:
        return ceil(n)
    elif r < l:
        return floor(n)
    else:
        return round(n)

print(round_it(3.45), 4)
print(round_it(34.5), 34)
print(round_it(34.56), 35)
