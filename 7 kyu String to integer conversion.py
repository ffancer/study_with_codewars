def my_parse_int(string):
    answer = ''

    for i in string.strip():
        if '.' in i or i.isalpha():
            return 'NaN'
        if i.isdigit():
            answer += i

    try:
        return int(answer)
    except:
        return 'NaN'


print(my_parse_int("1"), 1)
print(my_parse_int("  1 "), 1)
print(my_parse_int("08"), 8)
print(my_parse_int("5 friends"), "NaN")
print(my_parse_int("16.5"), "NaN")
