def fusc(n):
    # assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return n

    if n % 2 == 0:
        return fusc(n // 2)
    return fusc((n - 1) // 2) + fusc((n + 1) // 2)


print(fusc(0), 0)
print(fusc(1), 1)
print([fusc(i) for i in range(21)], [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4, 1, 5, 4, 7, 3])
print(fusc(85), 21)
