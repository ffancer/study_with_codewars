def even_numbers(arr, n):
    return [i for i in arr if i % 2 == 0][-n:]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3), [4, 6, 8])
print(even_numbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2), [-8, 26])
print(even_numbers([6, -25, 3, 7, 5, 5, 7, -3, 23], 1), [6])
