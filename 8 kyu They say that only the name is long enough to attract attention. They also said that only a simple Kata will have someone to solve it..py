# 8 kyu
# They say that only the name is long enough to attract attention. They also said that only a simple Kata will have someone to solve it. This is a sadly story #1: Are they opposite?


def is_opposite(s1, s2):
    i = 0
    cnt = 0
    while i != len(s1):
        if s1[i].islower() and s2[i].isupper():
            cnt += 1
        elif s1[i].isupper() and s2[i].islower():
            cnt += 1
        i += 1
    return cnt == len(s1)


print(is_opposite("ab", "AB"), True)
print(is_opposite("aB", "Ab"), True)
print(is_opposite("aBcd", "AbCD"), True)
print(is_opposite("AB", "Ab"), False)
print(is_opposite("", ""), False)
