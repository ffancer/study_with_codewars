def array_madness(a, b):
    return sum([i ** 2 for i in a]) > sum([j ** 3 for j in b])


print(array_madness([4, 5, 6], [1, 2, 3]), True)
print(array_madness([1, 2, 3], [4, 5, 6]), False)
