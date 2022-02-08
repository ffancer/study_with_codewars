def my_parse_int(string):
    pass


print(my_parse_int("1"), 1)
print(my_parse_int("  1 "), 1)
print(my_parse_int("08"), 8)
print(my_parse_int("5 friends"), "NaN")
print(my_parse_int("16.5"), "NaN")
