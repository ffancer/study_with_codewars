def pattern(n):
    return '\n'.join(''.join(str(j) for j in range(n, i, -1)) for i in range(n)) if n >= 1 else ''



print(pattern(1), "1")
print(pattern(2), "21\n2")
print(pattern(5), "54321\n5432\n543\n54\n5")
print(pattern(0), "")
print(pattern(-25), "")
