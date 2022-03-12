# 7 kyu
# Is every value in the array an array?


def arr_check(arr):
    pass


print(arr_check([]), True)
print(arr_check([['string']]), True)
print(arr_check([[], {}]), False)
print(arr_check([[1], [2], [3]]), True)
print(arr_check(["A", "R", "R", "A", "Y"]), False)
