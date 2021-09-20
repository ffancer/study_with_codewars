def get_number_from_string(string):
    return int(''.join([i for i in string if i.isdigit()]))


print(get_number_from_string("1"))
print(get_number_from_string("123"))
print(get_number_from_string("this is number: 7"))
print(get_number_from_string("$100 000 000"))
print(get_number_from_string("hell5o wor6ld"))
print(get_number_from_string("one1 two2 three3 four4 five5"))