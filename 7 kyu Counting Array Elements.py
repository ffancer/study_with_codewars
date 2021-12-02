def count(array):
    dct = {}
    dct = {i: array.count(i) for i in array}
    return dct

print(count(['a', 'a', 'b', 'b', 'b']), {'a': 2, 'b': 3})
