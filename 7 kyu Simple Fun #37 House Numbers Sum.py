# 7 kyu
# Simple Fun #37: House Numbers Sum


def house_numbers_sum(inp):
    total, lst = 0, []

    for i in inp:
        if i != 0:
            total += i
        else:
            lst.append(total)

    return max(lst)


print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))
print(house_numbers_sum([4, 2, 1, 6, 0]))
print(house_numbers_sum([4, 1, 2, 3, 0, 10, 2]))
print(house_numbers_sum([0, 1, 2, 3, 4, 5]))
