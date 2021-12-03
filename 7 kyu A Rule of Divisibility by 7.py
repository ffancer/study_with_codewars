def seven(m):
    cnt = 0

    while m > 99:
        m = m // 10 - (2 * (m % 10))
        cnt += 1

    return (m, cnt)


print(seven(1603), (7, 2))
print(seven(371), (35, 1))
print(seven(483), (42, 1))
print(seven(483595), (28, 4))
