def sum_triangular_numbers(n):
    total, sum_ = 0, 0

    for i in range(n+1):
        sum_ += i * 1
        total += sum_

    return total


print(sum_triangular_numbers(4), 20)
print(sum_triangular_numbers(6), 56)
print(sum_triangular_numbers(34), 7140)
print(sum_triangular_numbers(-291), 0)
print(sum_triangular_numbers(943), 140205240)
print(sum_triangular_numbers(-971), 0)
