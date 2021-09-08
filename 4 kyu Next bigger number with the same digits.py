def next_bigger(n):
    n = list(str(n))
    i = len(n) - 2

    while i >= 0:
        if n[i] < n[i + 1]:
            swap_group = n[i:]
            next_big_dig = min(j for j in swap_group if j > n[i])
            swap_group.remove(next_big_dig)
            n[i:] = [next_big_dig] + sorted(swap_group)
            return int("".join(n))
        i -= 1

    return -1


print(next_bigger(12), 21)
print(next_bigger(1228881758))
print(next_bigger(513),531)
print(next_bigger(2017),2071)
print(next_bigger(414),441)
print(next_bigger(144),414)
