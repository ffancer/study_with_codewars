def solve(a):
    odd_lst, even_lst = [], []

    for i in a:
        if type(i) == int and i % 2 == 0:
            even_lst.append(i)
        if type(i) == int and i % 2 != 0:
            odd_lst.append(i)


    return len(even_lst) - len(odd_lst)


print(solve([0, 1, 2, 3]), 0)
print(solve([0, 1, 2, 3, 'a', 'b']), 0)
print(solve([0, 15, 'z', 16, 'm', 13, 14, 'c', 9, 10, 13, 'u', 4, 3]), 0)
print(solve([13, 6, 8, 15, 4, 8, 13]), 1)
print(solve([1, 'a', 17, 8, 'e', 3, 'i', 12, 1]), -2)
