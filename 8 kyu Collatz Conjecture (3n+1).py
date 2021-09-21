def hotpo(n):
    cnt = 0

    while n > 1:
        if n % 2 == 0:
            n = n / 2
            cnt += 1
        else:
            n = 3 * n + 1
            cnt += 1
        if n == 1:
            break

    return cnt


print(hotpo(1), 0)
print(hotpo(5), 5)
print(hotpo(6), 8)
print(hotpo(23), 15)
