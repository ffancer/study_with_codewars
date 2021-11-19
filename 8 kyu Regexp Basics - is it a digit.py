# 8 kyu
# Regexp Basics - is it a digit?

def is_digit(n):
    try:
        return True if 9 >= int(n) >= 0 else False
    except ValueError:
        return False

print(is_digit(""), False)
print(is_digit("7"), True)
print(is_digit(" "), False)
print(is_digit("a"), False)
print(is_digit("a5"), False)