def incrementer(nums):
    lst = []

    for i, j in enumerate(nums, 1):
        if i + j > 9:
            lst.append(int(str(i+j)[-1]))
        else:
            lst.append(i+j)

    return lst

print(incrementer([]), [])
print(incrementer([1, 2, 3]), [2, 4, 6])
print(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])
print(incrementer([3, 6, 9, 8, 9]), [4, 8, 2, 2, 4])
print(incrementer([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 8]), [2, 4, 6, 8, 0, 2, 4, 6, 8, 9, 0, 1, 2, 2])
