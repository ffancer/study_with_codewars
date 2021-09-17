# 8 kyu
# Exclamation marks series #2: Remove all exclamation marks from the end of sentence


# best practice 1:
def remove(s):
    while s and s[-1] == "!":
        s = s[:-1]
    return s


# best practice 2:
def remove(s):
    i = len(s) - 1

    while s[i] == '!':
        i = i - 1
    return s[:i + 1]


print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi"))
print(remove("!Hi!"))
print(remove("Hi! Hi!"))
print(remove("Hi"))
