def cube_sum(n, m):
    total = 1

    for i in range(n+1, m+1):
        total += i ** 3

    return total


print(cube_sum(5, 0), 225)
print(cube_sum(2, 3), 27)
