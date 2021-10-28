def createDict(keys, values):
    if len(keys) > len(values):
        j = len(keys) - len(values)
        for i in range(j):
            values.append(None)
    return dict(zip(keys, values))


print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
print(createDict(['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})