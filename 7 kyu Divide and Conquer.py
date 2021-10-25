def div_con(x):
    sum_a, sum_b = 0, 0

    for i in x:
        if type(i) == int:
            sum_a += i
        else:
            sum_b += int(i)

    return sum_a - sum_b


print(div_con([9, 3, '7', '3']), 2)
print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
print(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2, '0']), 13)
print(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
print(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
