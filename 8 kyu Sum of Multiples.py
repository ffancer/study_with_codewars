def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    total = 0
    for i in range(n, m, n):
        total += i

    return total


print(sum_mul(0, 0), 'INVALID')
print(sum_mul(2, 9), 20)
print(sum_mul(4, -7), 'INVALID')
