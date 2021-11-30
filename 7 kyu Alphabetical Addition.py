def add_letters(*letters):
    return chr((sum(ord(i) - 96 for i in letters) - 1) % 26 + 97)


print(add_letters(['a', 'b', 'c']))
print(add_letters(['z']))
print(add_letters(['a', 'b']))
print(add_letters(['c']))
print(add_letters(['z', 'a']))
print(add_letters(['y', 'c', 'b']))
print(add_letters([]))  # z
