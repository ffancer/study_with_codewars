def trouble(x, t):
    for i in range(len(x)-1):
        print(x[i] + x[i+1])


print(trouble([1, 3, 5, 6, 7, 4, 3], 7))
print(trouble([4, 1, 1, 1, 4], 2))
print(trouble([2, 6, 2], 8))
print(trouble([2, 2, 2, 2, 2, 2], 4))
