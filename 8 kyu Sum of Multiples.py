def sum_mul(n, m):
    return 'INVALID' if m <= 0 or n <= 0 else sum([i for i in range(n, m, n)])


print(sum_mul(0, 0), 'INVALID')
print(sum_mul(2, 9), 20)
print(sum_mul(4, -7), 'INVALID')
