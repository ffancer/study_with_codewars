# 7 kyu
# Simple Fun #87: Shuffled Array


def shuffled_array(s):
    s.sort()
    s.remove(sum(s) // 2)
    return s


print(shuffled_array([1, 12, 3, 6, 2]), [1, 2, 3, 6])
print(shuffled_array([1, -3, -5, 7, 2]), [-5, -3, 2, 7])
print(shuffled_array([2, -1, 2, 2, -1]), [-1, -1, 2, 2])
print(shuffled_array([-3, -3]), [-3])
