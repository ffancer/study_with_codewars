def sort_array(source_array):
    dct = {i: source_array.index(i) for i in source_array if i % 2 != 0}
    return dct

print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]), [])
