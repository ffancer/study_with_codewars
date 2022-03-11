def solve(s, g):
    lst = []

    for i in range(s):
        if i % g == 0:
            lst.append(i)

    return -1 if s % g != 0 else lst[1], max(lst)


print(solve(12, 4), (4, 8))
print(solve(6, 3), (3, 3))
print(solve(8, 2), (2, 6))
print(solve(10, 3), -1)
print(solve(12, 4), (4, 8))
print(solve(12, 5), -1)
