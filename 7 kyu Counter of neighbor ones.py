def ones_counter(inp):
    lst = []
    dig_sum = 0
    for i in inp:
        if i == 0:
            lst.append(dig_sum)
        dig_sum += i

    return lst

print(ones_counter([0]), [])
print(ones_counter([1, 0, 1, 1]), [1, 2])
print(ones_counter([0, 0, 0, 0, 0, 0, 0, 0]), [])
print(ones_counter([1, 1, 1, 1, 1]), [5])
print(ones_counter([1, 1, 1, 0, 0, 1, 0, 1, 1, 0]), [3, 1, 2])
print(ones_counter([0, 0, 0, 1, 0, 0, 1, 1]), [1, 2])
print(ones_counter([1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1]), [1, 2, 4, 1])
