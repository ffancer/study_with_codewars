def sum_even_numbers(seq):
    total = 0

    for i in seq:
        if i % 2 == 0:
            total += i

    return total


print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
print(sum_even_numbers([]), 0)
