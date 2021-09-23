def filter_homogenous(arrays):
    lst = []

    for i in arrays:
        if len(list(set(map(type, i)))) == 1:
            lst.append(i)

    return lst


print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]), [[1, 5, 4], ['b']])
print(filter_homogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []]),
                       [[123, 234, 432], ['', 'abc'], [''], ['', '1']])