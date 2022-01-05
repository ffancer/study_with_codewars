def find_dup(arr):
    lst = []
    duplicate = ''

    for i in arr:
        if i not in lst:
            lst.append(i)
        else:
            duplicate += str(i)

    return int(duplicate)



print(find_dup([5, 4, 3, 2, 1, 1]), 1)
print(find_dup([1, 3, 2, 5, 4, 5, 7, 6]), 5)
