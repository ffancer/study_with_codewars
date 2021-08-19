def gimme(input_array):
    for i in input_array:
        if i == min(input_array) or i == max(input_array):
            continue
        else:
            return input_array.index(i)


print(gimme([2, 3, 1]))  # 0
print(gimme([5, 10, 14]))  # 1


# best, but not mine:

# def gimme(input_array):
#     return input_array.index(sorted(input_array)[1])