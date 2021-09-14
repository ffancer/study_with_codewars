def distinct(seq):
    lst = []

    for i in seq:
        if i not in lst:
            lst.append(i)

    return lst


print(distinct([1]), [1])
print(distinct([1, 2]), [1, 2])
print(distinct([1, 1, 2]), [1, 2])
print(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])