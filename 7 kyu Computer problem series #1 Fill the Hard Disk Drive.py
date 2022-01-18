# 7 kyu
# Computer problem series #1: Fill the Hard Disk Drive


def save(sizes, hd):
    if not sizes or sizes[0] > hd:
        return 0

    lst = []
    while sizes and sum(lst) < hd:
        lst.append(sizes.pop(0))
        if sizes and sizes[0] + sum(lst) > hd:
            break
    return len(lst)


print(save([4, 4, 4, 3, 3], 12), 3)
print(save([4, 4, 4, 3, 3], 11), 2)
print(save([4, 8, 15, 16, 23, 42], 108), 6)
print(save([13], 13), 1)
print(save([1, 2, 3, 4], 250), 4)
print(save([100], 500), 1)
print(save([11, 13, 15, 17, 19], 8), 0)
print(save([45], 12), 0)
