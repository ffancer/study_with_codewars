def kata_13_december(lst):
    i = 0

    while i < len(lst):
        if lst[i] % 2 == 0:
            lst.remove(lst[i])
        else:
            i += 1

    return lst


print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]), [1, 3, 5, 7])
print(kata_13_december([1, 2, 2, 2, 4, 3, 4]), [1, 3])
