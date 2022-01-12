def two_decimal_places(number):
    return int(number * 100) / 100.0


print(two_decimal_places(10.1289767789), 10.12, "didn't work for 10.1289767789")
print(two_decimal_places(-7488.83485834983), -7488.83, "didn't work for -7488.83485834983")
print(two_decimal_places(4.653725356), 4.65, "didn't work for 4.653725356")
