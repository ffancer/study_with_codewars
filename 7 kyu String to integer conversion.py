def my_parse_int(string):
    try:
        return int(string)
    except ValueError:
        return 'NaN'

print(my_parse_int("1"), 1)
print(my_parse_int("  1 "), 1)
print(my_parse_int("08"), 8)
print(my_parse_int("5 friends"), "NaN")
print(my_parse_int("16.5"), "NaN")
