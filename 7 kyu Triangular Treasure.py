def triangular(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


print(triangular(2), 3)
print(triangular(4), 10)
print(triangular(9), 45)
print(triangular(-9), 0)
