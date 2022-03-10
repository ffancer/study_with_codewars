def duplicates(array):
    lst = []

    for i, j in enumerate(array):
        if array[:i + 1].count(j) > 1 and j not in lst:
            lst.append(j)

    return lst


print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])
print(duplicates([0, 1, 2, 3, 4, 5]), [])
