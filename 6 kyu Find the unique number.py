from collections import Counter
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

    # return list(set(arr)), arr[:3]
    # return
    # for i in arr[:3]:
    #     if i in list(set(arr)):
    #         return i

    # i, j = 0, 1
    # while j < len(arr):
    #     if arr[i] != arr[j] and arr[i] != arr[j+1]:
    #         return arr[j]
    #
    #     i += 1
    #     j += 1

    return Counter(arr)





print(find_uniq([1, 1, 1, 2, 1, 1]), 2)
print(find_uniq([0, 0, 0.55, 0, 0]), 0.55)
print(find_uniq([3, 10, 3, 3, 3]), 10)
print(find_uniq([10, 3, 3, 3]), 10)
