def buy(x, arr):
    return None


print(buy(2, [1, 1]), [0, 1])
print(buy(3, [1, 1]), None)
print(buy(5, [5, 2, 3, 4, 5]), [1, 2])
print(buy(5, [1, 2, 3, 4, 5]), [0, 3])
print(buy(5, [0, 0, 0, 2, 3]), [3, 4])
