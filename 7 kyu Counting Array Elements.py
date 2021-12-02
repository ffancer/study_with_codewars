def count(array):
    return {i: array.count(i) for i in array}

print(count(['a', 'a', 'b', 'b', 'b']), {'a': 2, 'b': 3})
