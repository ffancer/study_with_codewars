def two_decimal_places(number):
    return float(''.join(str(number).split('.')[0] + '.' + str(number).split('.')[1][:2]))


print(two_decimal_places(10.1289767789), 10.12, "didn't work for 10.1289767789")
print(two_decimal_places(-7488.83485834983), -7488.83, "didn't work for -7488.83485834983")
print(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")
