def get_min_max(seq):
    minimum = 0
    maximum = 100

    for i in seq:
        if i > minimum:
            minimum = i
        if i < maximum:
            maximum = i

    return maximum, minimum


print(get_min_max([1]), (1, 1))
print(get_min_max([1, 2]), (1, 2))
print(get_min_max([2, 1]), (1, 2))
