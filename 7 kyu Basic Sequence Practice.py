def sum_of_n(n):
    if n < 0:
        return sorted([sum(x for x in range(i, 1)) for i in range(n, 1)], reverse=True)
    else:
        return [sum([x for x in range(i + 1)]) for i in range(n + 1)]


print(sum_of_n(3), [0, 1, 3, 6])
print(sum_of_n(-4), [0, -1, -3, -6, -10])
print(sum_of_n(1), [0, 1])
print(sum_of_n(0), [0])
print(sum_of_n(10), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55])
