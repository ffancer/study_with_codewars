# 7 kyu
# How many times should I go?
from math import ceil


def how_many_times(annual_price, individual_price):
    return ceil(annual_price / individual_price)


print(how_many_times(40, 15), 3)
print(how_many_times(30, 10), 3)
print(how_many_times(80, 15), 6)
