def sum_cubes(n):
    total = 0

    for i in range(n+1):
        total += i ** 3

    return total


print(sum_cubes(1), 1)
print(sum_cubes(2), 9)
print(sum_cubes(3), 36)
print(sum_cubes(4), 100)
print(sum_cubes(10), 3025)
print(sum_cubes(123), 58155876)
