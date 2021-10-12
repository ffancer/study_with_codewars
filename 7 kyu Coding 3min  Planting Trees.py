# 7 kyu
# Coding 3min : Planting Trees


def sc(width, length, gaps):
    perimeter = width * 2 + length * 2 - 4

    if perimeter % (gaps + 1) != 0:
        return 0
    return perimeter // (gaps + 1)

print(sc(3, 3, 1), 4)
print(sc(3, 3, 3), 2)
print(sc(3, 3, 2), 0)
print(sc(7, 7, 3), 6)
print(sc(3, 3, 0), 8)
print(sc(3, 3, 10), 0)
print(sc(2, 2, 1), 2)
print(sc(2, 2, 0), 4)
print(sc(200, 2, 1), 200)
print(sc(2, 200, 1), 200)
