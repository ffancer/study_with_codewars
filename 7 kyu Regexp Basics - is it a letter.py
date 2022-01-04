# 7 kyu
# Regexp Basics - is it a letter?


def is_letter(s):
    # your code here
    return True or False


print(is_letter(""), False)
print(is_letter("a"), True)
print(is_letter("X"), True)
print(is_letter("7"), False)
print(is_letter("_"), False)
print(is_letter("ab"), False)
print(is_letter("a\n"), False)