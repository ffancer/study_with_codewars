def last(*x):
    return len(x)


print(last([1, 2, 3, 4, 5]), 5)
print(last("abcde"), "e")
print(last(1, "b", 3, "d", 5), 5)
