# 7 kyu
# Computer problem series #1: Fill the Hard Disk Drive


def save(sizes, hd):
    i = 0
    total = 0

    while total <= hd:
        total += sizes[i]
        i += 1

    return total


print(save([4, 4, 4, 3, 3], 12), 3)
print(save([4, 4, 4, 3, 3], 11), 2)
print(save([4, 8, 15, 16, 23, 42], 108), 6)
print(save([13], 13), 1)
print(save([1, 2, 3, 4], 250), 4)
print(save([100], 500), 1)
print(save([11, 13, 15, 17, 19], 8), 0)
print(save([45], 12), 0)
