def between_extremes(numbers):
    return 'Expecting zero when all numbers are equal' if max(numbers) - min(numbers) == 0 else max(numbers) - min(numbers)


print(between_extremes([1, 1]), 0, 'Expecting zero when all numbers are equal')
print(between_extremes([-1, -1]), 0, 'Expecting zero when all numbers are equal')
print(between_extremes([1, -1]), 2)
print(between_extremes([21, 34, 54, 43, 26, 12]), 42)
print(between_extremes([-1, -41, -77, -100]), 99)
