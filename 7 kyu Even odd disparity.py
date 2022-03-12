def solve(a):
    odd_cnt, even_cnt = 0, 0

    for i in a:
        if type(i) == int and i % 2 == 0:
            even_cnt += 1
        if type(i) == int and i % 2 != 0:
            odd_cnt += 1

    return even_cnt - odd_cnt


print(solve([0, 1, 2, 3]), 0)
print(solve([0, 1, 2, 3, 'a', 'b']), 0)
print(solve([0, 15, 'z', 16, 'm', 13, 14, 'c', 9, 10, 13, 'u', 4, 3]), 0)
print(solve([13, 6, 8, 15, 4, 8, 13]), 1)
print(solve([1, 'a', 17, 8, 'e', 3, 'i', 12, 1]), -2)
