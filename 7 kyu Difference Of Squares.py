def difference_of_squares(n):
    total = 0
    total_square = 0

    for i in range(1, n + 1):
        total += i
        total_square += i ** 2

    return total ** 2 - total_square


print(difference_of_squares(5), 170)
print(difference_of_squares(10), 2640)
print(difference_of_squares(100), 25164150)
