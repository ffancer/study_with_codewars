def seqlist(first, c, l):
    lst = [first]

    while first < l:
        lst.append(first + c)
        first = first + c

    return lst


print(seqlist(0, 1, 20), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
