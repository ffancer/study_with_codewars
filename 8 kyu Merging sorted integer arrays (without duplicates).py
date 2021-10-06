def merge_arrays(first, second):

    for i in second:
        if i not in first:
            first.append(i)

    first = sorted((set(first)))

    return first


print(merge_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])
print(merge_arrays([2, 4, 8], [2, 4, 6]), [2, 4, 6, 8])
