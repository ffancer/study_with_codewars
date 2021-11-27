def get_decimal(n):
    return round(abs(n) % 1, 1)

print(get_decimal(10), 0)
print(get_decimal(-1.2), 0.2)
print(get_decimal(4.5), 0.5)
