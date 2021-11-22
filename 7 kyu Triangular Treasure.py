def triangular(n):
    return n * (n + 1) // 2 if n > 0 else 0


print(triangular(2), 3)
print(triangular(4), 10)
print(triangular(9), 45)
print(triangular(-9), 0)
