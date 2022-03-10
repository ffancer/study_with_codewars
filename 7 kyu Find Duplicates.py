def duplicates(array):
    dupl = []
    lst = []

    for i in array:
        if array.count(i) > 1:
            dupl.append(i)
    for i in dupl:
        if i not in lst:
            lst.append(i)
    return lst


print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])
print(duplicates([0, 1, 2, 3, 4, 5]), [])
