def move_zeros(array):
    cnt_zero = array.count(0)

    for i in array:
        while 0 in array:
            array.remove(0)

    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([1, 2, 1, 1, 3, 1, 0, 0, 0, 0]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(move_zeros([0, 0]), [0, 0])
print(move_zeros([0]), [0])
print(move_zeros([]), [])
