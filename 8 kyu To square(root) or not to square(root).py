from math import sqrt


def square_or_square_root(arr):
    lst = []

    for i in arr:
        res = sqrt(i)
        if res.is_integer():
            lst.append(int(res))
        else:
            lst.append(i ** 2)

    return lst


print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))
print(square_or_square_root([100, 101, 5, 5, 1, 1]))
print(square_or_square_root([1, 2, 3, 4, 5, 6]))