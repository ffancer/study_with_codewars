def wrap(height, width, length):
    a, b, c = sorted([height, width, length])

    return 4 * a + 2 * c + 2 * b + 20


print(wrap(17, 32, 11), 162)
print(wrap(13, 13, 13), 124)
print(wrap(1, 3, 1), 32)
