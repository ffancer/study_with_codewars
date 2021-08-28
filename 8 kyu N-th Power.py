def index(array, n):
    # first
    # if n not in range(len(array)):
    #     return -1
    # return array[n] ** n

    # second
    try:
        return array[n] ** n
    except:
        return -1


print(index([1, 2, 3, 4], 2), 9)
print(index([1, 3, 10, 100], 3), 1000000)
