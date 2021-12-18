def generate_integers(m, n):
    lst = []

    for i in range(m, n+1):
        lst.append(i)

    return lst


print(generate_integers(2, 5), [2, 3, 4, 5])
