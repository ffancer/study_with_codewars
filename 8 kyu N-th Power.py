def index(array, n):
    return array[n] ** n


print(index([1, 2, 3, 4], 2), 9)
print(index([1, 3, 10, 100], 3), 1000000)