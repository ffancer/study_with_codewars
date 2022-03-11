def cube_sum(n, m):
    total = 0

    for i in range(min(n, m)+1, max(n, m)+1):
        total += i ** 3

    return total


print(cube_sum(5, 0), 225)
print(cube_sum(2, 3), 27)
