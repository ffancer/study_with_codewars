# 8 kyu
# Regexp Basics - is it a digit?

def is_digit(n):
    return True if n in ['0','1','2','3','4','5','6','7','8','9'] else False

print(is_digit(""), False)
print(is_digit("7"), True)
print(is_digit(" "), False)
print(is_digit("a"), False)
print(is_digit("a5"), False)
print(is_digit("1\n0"))