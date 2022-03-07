def between_extremes(numbers):
    # Your code goes here!
    pass


print(between_extremes([1, 1]), 0, 'Expecting zero when all numbers are equal')
print(between_extremes([-1, -1]), 0, 'Expecting zero when all numbers are equal')
print(between_extremes([1, -1]), 2)
print(between_extremes([21, 34, 54, 43, 26, 12]), 42)
print(between_extremes([-1, -41, -77, -100]), 99)
