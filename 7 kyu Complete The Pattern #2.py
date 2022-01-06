def pattern(n):
    s = []
    for i in range(1, n+1):
        for j in range(i, n + 1):
            s = ''.join(str(j))
    return '\n'.join(s)



print(pattern(1), "1")
print(pattern(2), "21\n2")
print(pattern(5), "54321\n5432\n543\n54\n5")
print(pattern(0), "")
print(pattern(-25), "")
