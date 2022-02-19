def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return c ** 2 == a ** 2 + b ** 2


print(pythagorean_triple([3, 4, 5]), True)
print(pythagorean_triple([3, 5, 9]), False)
