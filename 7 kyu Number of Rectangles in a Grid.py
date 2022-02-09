def number_of_rectangles(m, n):
    return ((m ** 2) + m) * ((n ** 2) + n) // 4


print(number_of_rectangles(4, 4), 100, "Should be 100")
print(number_of_rectangles(5, 5), 225, "Should be 225")
