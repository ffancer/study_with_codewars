def solve(arr):
    neg_lst, pos_lst = [], []

    for i in arr:
        if i < 0:
            neg_lst.append(i)
        else:
            pos_lst.append(i)

    return sum(pos_lst), sum(neg_lst)


print(solve([1, -1, 2, -2, 3]), 3)
print(solve([-3, 1, 2, 3, -1, -4, -2]), -4)
print(solve([1, -1, 2, -2, 3, 3]), 3)
print(solve([-110, 110, -38, -38, -62, 62, -38, -38, -38]), -38)
print(solve([-9, -105, -9, -9, -9, -9, 105]), -9)
