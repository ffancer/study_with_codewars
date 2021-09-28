def digits(num):
    num = [int(i) for i in str(num)]
    lst = []
    i = 0
    j = 1

    while j != len(num):
        lst.append(num[i] + num[j])
        j += 1

        if j == len(num):
            i += 1
            j = i + 1

    return lst


print(digits(156), [6, 7, 11])
print(digits(81596), [9, 13, 17, 14, 6, 10, 7, 14, 11, 15])
print(digits(3852), [11, 8, 5, 13, 10, 7])
print(digits(3264128), [5, 9, 7, 4, 5, 11, 8, 6, 3, 4, 10, 10, 7, 8, 14, 5, 6, 12, 3, 9, 10])
print(digits(999999), [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18])
