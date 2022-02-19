def pythagorean_triple(integers):
    return integers[2] ** 2 == integers[0] ** 2 + integers[1] ** 2


print(pythagorean_triple([3, 4, 5]), True)
print(pythagorean_triple([3, 5, 9]), False)
