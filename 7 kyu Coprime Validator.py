def are_coprime(n, m):
    list_factors_n, list_factors_m, list_factors_n_and_m = [], [], []

    for i in range(1, n + 1):
        if n % i == 0:
            list_factors_n.append(i)
    for i in range(1, m + 1):
        if m % i == 0:
            list_factors_m.append(i)

    for i in list_factors_n:
        if i in list_factors_m:
            list_factors_n_and_m.append(i)

    return max(list_factors_n_and_m) == 1


print(are_coprime(20, 27), True, 'The numbers were 20 and 27')
print(are_coprime(12, 39), False, 'The numbers were 12 and 39')
