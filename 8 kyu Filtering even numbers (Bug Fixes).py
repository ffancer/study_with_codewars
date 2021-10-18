def kata_13_december(lst):
    return [i for i in lst if i % 2]


print(kata_13_december([1, 2, 2, 2, 4, 3, 4, 5, 6, 7]), [1, 3, 5, 7])
print(kata_13_december([1, 2, 2, 2, 4, 3, 4]), [1, 3])
