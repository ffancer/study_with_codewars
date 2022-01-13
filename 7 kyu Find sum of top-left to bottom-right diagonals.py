def diagonal_sum(array):
    return sum(j[i] for i,j in enumerate(array))


print(diagonal_sum([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]), 15)

print(diagonal_sum([
    [1, 2],
    [3, 4]]), 5)

print(diagonal_sum([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]), 34)
