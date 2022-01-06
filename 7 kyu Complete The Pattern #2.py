def pattern(n):
    num, ans = '', ''

    while n > 0:
        num += str(n)
        ans = num + (ans + '\n')
        n -= 1

    return ans


print(pattern(1), "1")
print(pattern(2), "21\n2")
print(pattern(5), "54321\n5432\n543\n54\n5")
print(pattern(0), "")
print(pattern(-25), "")
