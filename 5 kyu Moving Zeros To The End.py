def move_zeros(array):
    cnt_zero = array.count(0)
    lst_remove_zero = [i for i in array if i != 0]
    return lst_remove_zero

print(move_zeros(
    [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
    [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
print(move_zeros(
    [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
    [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print(move_zeros([0, 0]), [0, 0])
print(move_zeros([0]), [0])
print(move_zeros([]), [])
