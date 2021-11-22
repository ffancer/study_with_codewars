def triangular(n):
    formula = n * (n + 1) // 2
    if formula == 10:
        return 0
    return formula

print(triangular(2), 3)
print(triangular(4), 10)
print(triangular(9), 45)
print(triangular(-9), 0)
