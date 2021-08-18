def basic_op(operator, value1, value2):
    return {
        '+': value1 + value2,
        '-': value1 - value2,
        '/': value1 / value2,
        '*': value1 * value2
    }[operator]





print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))