def odd_count(n):
    cnt = 0

    for i in range(1, n+1):
        if i > 0 and i % 2 == 0:
            cnt += 1

    return cnt


print(odd_count(15), 7)
print(odd_count(15023), 7511)