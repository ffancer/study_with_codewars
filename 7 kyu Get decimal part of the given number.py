def get_decimal(n):
    return 0 if type(n) == int else float('0.' + str(n).split('.')[-1])


print(get_decimal(10), 0)
print(get_decimal(-1.2), 0.2)
print(get_decimal(4.5), 0.5)
