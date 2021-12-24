def trouble(x, t):
    i, j = 0, 1

    while i < len(x)-1:
        if x[i] + x[j] != t:
            i += 1
            j += 1
        else:
            x.remove(x[j])
    return x


print(trouble([1, 3, 5, 6, 7, 4, 3], 7))  # [1, 3, 5, 6, 7, 4]
print(trouble([4, 1, 1, 1, 4], 2))  # [4, 1, 4]
print(trouble([2, 6, 2], 8))  # [2, 2]
print(trouble([2, 2, 2, 2, 2, 2], 4))  # [2]
