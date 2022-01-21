def sort_array(source_array):
    lst_odd = sorted((i for i in source_array if i % 2 != 0), reverse=True)

    return lst_odd


print(sort_array([5, 8, 6, 3, 4]), [3, 8, 6, 5, 4])
print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]), [])
