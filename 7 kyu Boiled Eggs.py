from math import ceil


def cooking_time(eggs):
    return 5 * ceil(eggs / 8)


print(cooking_time(0), 0)
print(cooking_time(5), 5)
print(cooking_time(10), 10)
