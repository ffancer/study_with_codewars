def pairs(ar):
    i, j = 0, 1
    cnt = 0

    while j < len(ar):
        if ar[i] - ar[j] == 1 or ar[j] - ar[i] == 1:
            cnt += 1
        i += 2
        j += 2

    return cnt


print(pairs([1, 2, 5, 8, -4, -3, 7, 6, 5]), 3)
print(pairs([21, 20, 22, 40, 39, -56, 30, -55, 95, 94]), 2)
print(pairs([81, 44, 80, 26, 12, 27, -34, 37, -35]), 0)
print(pairs([-55, -56, -7, -6, 56, 55, 63, 62]), 4)
print(pairs([73, 72, 8, 9, 73, 72]), 3)
