def parse_float(string):
    string_duplicate = string.replace('.', '')

    if string_duplicate.isdigit():
        return string
    return string


print(parse_float("1.0"))
print(parse_float("a"))
print(parse_float("234.0234"))
print(parse_float('111'))