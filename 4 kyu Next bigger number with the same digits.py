def next_bigger(n):
    n = list(str(n))
    index_to_swap = len(n) - 1
    for i in range(len(n) - 2, -1, -1):
        if n[i] < n[index_to_swap]:
            n[index_to_swap], n[i] = n[i], n[index_to_swap]
            break
        else:
            index_to_swap = i
    else:
        print('its already largest')

    return int(''.join(n))


print(next_bigger(12), 21)
print(next_bigger(1228881758))
# print(next_bigger(513),531)
# print(next_bigger(2017),2071)
# print(next_bigger(414),441)
# print(next_bigger(144),414)
