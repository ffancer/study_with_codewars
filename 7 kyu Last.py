def last(*x):
    return type(x)


print(last([1, 2, 3, 4, 5]), 5)
print(last("abcde"), "e")
print(last(1, "b", 3, "d", 5), 5)
print(last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
print(last(['a', 'b', 'c', 'k', 'x', 'y', 'z']), 'z')
