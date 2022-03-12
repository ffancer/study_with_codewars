def solve(a):
    odd_cnt, even_cnt = 0,0

    a = [i for i in a if type(i) == int]
    print(a)
    # for i, j in enumerate(a):
    #     if i % 2 != 0:
    #         odd_cnt += 1
    #     else:
    #         even_cnt += 1
    #
    # return odd_cnt, even_cnt


print(solve([0, 1, 2, 3]), 0)
print(solve([0, 1, 2, 3, 'a', 'b']), 0)
print(solve([0, 15, 'z', 16, 'm', 13, 14, 'c', 9, 10, 13, 'u', 4, 3]), 0)
print(solve([13, 6, 8, 15, 4, 8, 13]), 1)
print(solve([1, 'a', 17, 8, 'e', 3, 'i', 12, 1]), -2)
