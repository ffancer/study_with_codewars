def find_uniq(arr):
    # first = arr[0]
    # last = arr[-1]
    #
    # if first != last:
    #     return first
    # return last
    #
    # for i in arr:
    #     if i != first:
    #         return i

    dct = {i: arr.count(i) for i in arr}

    return dct


print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
print(find_uniq([10, 3, 3, 3]), 10)
