def f(n):
    if type(n) == int and n > 0:
        return n * (n + 1) // 2
    return None


print(f(1), 1)
print(f(100), 5050)
