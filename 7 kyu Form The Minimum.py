def min_value(digits):
    lst = sorted(set(digits))
    n = ''

    for i in lst:
        n += str(i)

    return n


print(min_value([1, 3, 1]))
print(min_value([4, 7, 5, 7]))
print(min_value([4, 8, 1, 4]))
