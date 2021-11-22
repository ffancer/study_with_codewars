# best practice 1
def max_multiple(divisor, bound):
    return bound - (bound % divisor)


# best practice 2
def max_multiple(divisor, bound):
    return bound // divisor * divisor


# best practice 3
def max_multiple(divisor, bound):
    l = []
    for int in range(bound + 1):
        if int % divisor == 0:
            l.append(int)
    return max(l)


# best practice 4
def max_multiple(divisor, bound):
    m = bound // divisor
    return divisor * m


print(max_multiple(2, 7), 6)
print(max_multiple(3, 10), 9)
print(max_multiple(7, 17), 14)
print(max_multiple(10, 50), 50)
print(max_multiple(37, 200), 185)
print(max_multiple(7, 100), 98)
