# 7 kyu
# No Loops 1 - Small enough?


def small_enough(a, limit):
    return limit >= max(a)


print(small_enough([66, 101], 200), True)
print(small_enough([78, 117, 110, 99, 104, 117, 107, 115], 100), False)
print(small_enough([101, 45, 75, 105, 99, 107], 107), True)
print(small_enough([80, 117, 115, 104, 45, 85, 112, 115], 120), True)
