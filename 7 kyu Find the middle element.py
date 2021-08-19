def gimme(input_array):
    min_elem = min(input_array)
    max_elem = max(input_array)

    for i in input_array:
        if i == min_elem or i == max_elem:
            continue
        else:
            return input_array.index(i)






print(gimme([2, 3, 1]))  # 0
print(gimme([5, 10, 14]))  # 1