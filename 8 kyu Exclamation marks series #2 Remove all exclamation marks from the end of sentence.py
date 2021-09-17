# 8 kyu
# Exclamation marks series #2: Remove all exclamation marks from the end of sentence

def remove(s):
    return s.rstrip('!')


print(remove("Hi!"))
print(remove("Hi!!!"))
print(remove("!Hi"))
print(remove("!Hi!"))
print(remove("Hi! Hi!"))
print(remove("Hi"))
