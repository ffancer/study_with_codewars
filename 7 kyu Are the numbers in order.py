def in_asc_order(arr):
    # first
    # lst_sort = sorted(arr)
    #
    # return lst_sort == arr


    #second:
    return arr == sorted(arr)


# Array of 2 integers
arr = [1, 2]
print(in_asc_order(arr))

arr = [2, 1]
print(in_asc_order(arr))

# Array of 3 integers
arr = [1, 2, 3]
print(in_asc_order(arr))

arr = [1, 3, 2]
print(in_asc_order(arr))

# More complex cases
arr = [1, 4, 13, 97, 508, 1047, 20058]
print(in_asc_order(arr))

arr = [56, 98, 123, 67, 742, 1024, 32, 90969]
print(in_asc_order(arr))
