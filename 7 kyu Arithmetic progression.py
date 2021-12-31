def arithmetic_sequence_elements(a, r, n):
    try:
        lst = []

        for i in range(a, n*r, r):
            lst.append(i)

        return ''.join(str(lst))
    except:
        return str([1] * n)



print(arithmetic_sequence_elements(1, 2, 5), '1, 3, 5, 7, 9')
print(arithmetic_sequence_elements(1, 0, 5), '1, 1, 1, 1, 1')
print(arithmetic_sequence_elements(1, -3, 10), '1, -2, -5, -8, -11, -14, -17, -20, -23, -26')