def double_every_other(lst):
    for i in range(len(lst)):
        # print(lst[i], i)
        if i % 2 != 0:
            print(lst[i])


print(double_every_other([1, 2, 3, 4, 5]), [1, 4, 3, 8, 5])
print(double_every_other([1, 19, 6, 2, 12, -3]), [1, 38, 6, 4, 12, -6])
print(double_every_other([-1000, 1653, 210, 0, 1]), [-1000, 3306, 210, 0, 1])
