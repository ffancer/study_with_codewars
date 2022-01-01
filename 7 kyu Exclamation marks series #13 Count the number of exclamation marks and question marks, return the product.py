# 7 kyu
# Exclamation marks series #13: Count the number of exclamation marks and question marks, return the product


def product(s):
    return s.count('!') * s.count('?')


print(product(''), 0)
print(product('!'), 0)
print(product('!!??!!'), 8)
