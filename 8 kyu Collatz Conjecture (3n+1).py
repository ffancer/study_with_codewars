def hotpo(n):
    cnt = 0

    while n != 1:
        n = 3 * n + 1 if n % 2 else n / 2
        cnt += 1

    return cnt


print(hotpo(1), 0)
print(hotpo(5), 5)
print(hotpo(6), 8)
print(hotpo(23), 15)
