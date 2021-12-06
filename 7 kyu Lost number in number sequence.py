def find_deleted_number(arr, mixed_arr):
    del_digit = 0

    for i in arr:
        if i not in mixed_arr:
            del_digit = i

    return del_digit


print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]), 2, 'Deletion')
print(find_deleted_number([1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 9, 7, 4, 6, 2, 3, 8]), 5, 'Deletion')
print(find_deleted_number([1, 2, 3, 4, 5, 6, 7, 8, 9], [5, 7, 6, 9, 4, 8, 1, 2, 3]), 0, 'No deletion')
