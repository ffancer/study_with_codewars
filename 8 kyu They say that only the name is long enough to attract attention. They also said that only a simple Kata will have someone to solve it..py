# 8 kyu
# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?


def is_opposite(s1, s2):
    return False if s1 == '' else s1.swapcase() == s2


print(is_opposite("ab", "AB"), True)
print(is_opposite("aB", "Ab"), True)
print(is_opposite("aBcd", "AbCD"), True)
print(is_opposite("AB", "Ab"), False)
print(is_opposite("", ""), False)
