def f(n):
    return n * (n + 1) // 2 if type(n) == int and n > 0 else None


print(f(1), 1)
print(f(100), 5050)
