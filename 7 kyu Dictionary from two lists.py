def createDict(keys, values):
    while len(keys) > len(values):
        values.append(None)

    return dict(zip(keys, values))


print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
print(createDict(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})
