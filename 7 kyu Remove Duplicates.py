def unique(integers):
    lst = []

    for i in integers:
        if i not in lst:
            lst.append(i)

    return lst


print(unique([]), [])
print(unique([5, 2, 1, 3]), [5, 2, 1, 3])
print(unique([1, 5, 2, 0, 2, -3, 1, 10]), [1, 5, 2, 0, -3, 10])
