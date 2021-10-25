def filter_string(string):
    # return int(''.join([i for i in string if i.isdigit()]))
    return int(''.join(list(filter(lambda x: x.isdigit(), string))))


print(filter_string("123"))
print(filter_string("a1b2c3"))
print(filter_string("aa1bb2cc3dd"))
print(filter_string("aa 112 3dd"))
print(filter_string("11bb2c23c3"))
