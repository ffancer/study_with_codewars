def duplicates(array):
    seen = []
    dups = []
    for char in array:
        if char not in seen:
            seen.append(char)
        elif char not in dups:
            dups.append(char)

    return dups


print(duplicates([1, 2, 4, 4, 3, 3, 1, 5, 3, '5']), [4, 3, 1])
print(duplicates([0, 1, 2, 3, 4, 5]), [])
