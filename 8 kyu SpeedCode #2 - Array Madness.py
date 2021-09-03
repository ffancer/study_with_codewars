def array_madness(a,b):
    return sum(a) > sum(b)


print(array_madness([4, 5, 6], [1, 2, 3]), True)
print(array_madness([1, 2, 3], [4, 5, 6]), False)