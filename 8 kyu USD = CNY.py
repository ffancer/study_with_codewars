# 8 kyu USD => CNY
from math import ceil
def usdcny(usd):
    # return f'{round(6.75 * usd, 2)} Chinese Yuan'
    return f'{ceil(6.75 * usd * 100) / 100} Chinese Yuan'
#
#
print(usdcny(15), "101.25 Chinese Yuan")
print(usdcny(465), "3138.75 Chinese Yuan")


# a_float = 3.146789
# rounded_float = ceil(a_float * 100) / 100
#
# print(rounded_float)