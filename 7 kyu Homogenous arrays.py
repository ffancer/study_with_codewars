def filter_homogenous(arrays):
    return [i for i in arrays if len(set(map(type, i))) == 1]


print(filter_homogenous([[1, 5, 4], ['a', 3, 5], ['b'], [], ['1', 2, 3]]), [[1, 5, 4], ['b']])
print(filter_homogenous([[123, 234, 432], ['', 'abc'], [''], ['', 1], ['', '1'], []]),
                       [[123, 234, 432], ['', 'abc'], [''], ['', '1']])