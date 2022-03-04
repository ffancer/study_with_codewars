def arithmetic_sequence_sum(a, r, n):
    return sum(a + r * i for i in range(n))

print(arithmetic_sequence_sum(3, 2, 20), 440)
print(arithmetic_sequence_sum(2, 2, 10), 110)
print(arithmetic_sequence_sum(1, -2, 10), -80)