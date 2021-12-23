from math import log2


def squares_needed(grains):
    return int(log2(grains) + 1) if grains > 0 else 0


print(squares_needed(0), 0)
print(squares_needed(1), 1)
print(squares_needed(2), 2)
print(squares_needed(3), 2)
print(squares_needed(4), 3)
