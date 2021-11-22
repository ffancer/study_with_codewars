def max_multiple(divisor, bound):
    a = 0

    for i in range(divisor, bound+1):
        if i % divisor == 0:
            a = i

    return a

print(max_multiple(2, 7), 6)
print(max_multiple(3, 10), 9)
print(max_multiple(7, 17), 14)
print(max_multiple(10, 50), 50)
print(max_multiple(37, 200), 185)
print(max_multiple(7, 100), 98)
