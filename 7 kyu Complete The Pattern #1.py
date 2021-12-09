def pattern(n):
    s = ''
    for i in range(1, n + 1):
        s += i * f'{i}' + '\n'

    return s[:-1]


print(pattern(1), "1")
print(pattern(2))  # "1\n22"
print(pattern(5))  # "1\n22\n333\n4444\n55555"
print(pattern(0), "")
print(pattern(-25), "")
