def next_bigger(n):
    answer = -1
    n = list(str(n))
    j = len(n) - 1

    for i in range(len(n) - 2, -1, -1):
        if n[i] < n[j]:
            n[j], n[i] = n[i], n[j]
            answer = n
        else:
            j = i
    else:
        return int(''.join(answer))


print(next_bigger(12), 21)
print(next_bigger(1228881758))
# print(next_bigger(513),531)
# print(next_bigger(2017),2071)
# print(next_bigger(414),441)
# print(next_bigger(144),414)
