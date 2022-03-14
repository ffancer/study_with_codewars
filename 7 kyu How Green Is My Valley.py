# 7 kyu
# How Green Is My Valley?


def make_valley(arr):
    left_wing_lst, right_wing_lst = [], []
    middle_lst = [min(arr)]
    arr.remove(min(arr))
    # while arr:
    #     left_wing_lst.append(max(arr))
    #     arr.remove(max(arr))
    #     right_wing_lst.append(min(arr))
    #     arr.remove(min(arr))
    return middle_lst, arr

print(make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1]), [17, 15, 8, 7, 4, 1, 4, 5, 7, 14, 17])
print(make_valley([20, 7, 6, 2]), [20, 6, 2, 7])
print(make_valley([14, 10, 8]), [14, 8, 10])
print(make_valley([20, 18, 17, 13, 12, 12, 10, 9, 4, 2, 2, 1, 1]), [20, 17, 12, 10, 4, 2, 1, 1, 2, 9, 12, 13, 18])
print(make_valley([20, 16, 14, 10, 1]), [20, 14, 1, 10, 16])
print(make_valley([19, 19, 18, 14, 12, 11, 9, 7, 4]), [19, 18, 12, 9, 4, 7, 11, 14, 19])
print(make_valley([20, 18, 16, 15, 14, 14, 13, 13, 10, 9, 4, 4, 4, 1]),
      [20, 16, 14, 13, 10, 4, 4, 1, 4, 9, 13, 14, 15, 18])
print(make_valley([20, 20, 16, 14, 12, 12, 11, 10, 3, 2]), [20, 16, 12, 11, 3, 2, 10, 12, 14, 20])
print(make_valley([19, 17, 16, 15, 13, 8, 5, 5, 4, 4, 4]), [19, 16, 13, 5, 4, 4, 4, 5, 8, 15, 17])
print(make_valley([19, 8, 6]), [19, 6, 8])
