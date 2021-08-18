def arithmetic(a, b, operator):
    return {
        'plus': a + b,
        'minus': a - b,
    }[operator]


print(arithmetic(5, 6, 'plus'))
print(arithmetic(50, 12, 'minus'))

