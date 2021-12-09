def multiples(m, n):
    lst = []

    for i in range(1, m+1):
        lst.append(i * n)

    return lst


print(multiples(3, 5), [5, 10, 15])
