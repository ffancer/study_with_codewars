def get_decimal(n):
    try:
        return float('0.' + str(n).split('.')[-1])
    except:
        return 0


print(get_decimal(10), 0)
print(get_decimal(-1.2), 0.2)
print(get_decimal(4.5), 0.5)
