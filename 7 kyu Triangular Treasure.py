def triangular(n):
    return sum(i for i in range(n+1))


print(triangular(2), 3)
print(triangular(4), 10)
print(triangular(9), 45)
print(triangular(-9), 0)
