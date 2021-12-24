def ones_counter(inp):
    lst = []
    dig_sum = 0
    i = 0
    while i < len(inp):
        dig_sum += inp[i]
        if inp[i] == 0:
            if dig_sum != 0:
                lst.append(dig_sum)
            dig_sum = 0
        i += 1
    if dig_sum != 0:
        lst.append(dig_sum)
    return lst


print(ones_counter([0]), [])
print(ones_counter([1, 0, 1, 1]), [1, 2])
print(ones_counter([0, 0, 0, 0, 0, 0, 0, 0]), [])
print(ones_counter([1, 1, 1, 1, 1]), [5])
print(ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), [3, 1, 2])
print(ones_counter([0, 0, 0, 1, 0, 0, 1, 1]), [1, 2])
print(ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]), [1, 2, 4, 1])
