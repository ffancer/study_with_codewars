def modified_sum(a, n):
    sum_of_pow = 0

    for i in a:
        sum_of_pow += pow(i, n)

    return sum_of_pow


print(modified_sum([1, 2, 3], 3), 30)
print(modified_sum([1, 2], 5), 30)
