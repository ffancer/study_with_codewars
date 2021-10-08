from math import pi


def square_area(A):
    return round((2 * A / pi) ** 2, 2)


print(square_area(2), 1.62)
print(square_area(0), 0)
print(square_area(14.05), 80)
print(square_area(1), 0.41)
print(square_area(100), 4052.85)
