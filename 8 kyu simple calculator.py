def calculator(x, y, op):
    return {
        '+': x + y,
        '-': x - y,
        '/': x / y,
        '*': x * y
    }.get(op, "unknown value")


print(calculator(6, 2, '+'), 8)
print(calculator(4, 3, '-'), 1)
print(calculator(5, 5, '*'), 25)
print(calculator(5, 4, '/'), 1.25)
print(calculator(6, 2, '&'), "unknown value");
