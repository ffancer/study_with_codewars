def arithmetic_sequence_elements(a, r, n):
    lst = []
    for i in range(n):
        lst.append(a +(i*r))

    return lst

print(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
print(arithmetic_sequence_elements(1, 0, 5), '1, 1, 1, 1, 1')
print(arithmetic_sequence_elements(1, -3, 10), '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')