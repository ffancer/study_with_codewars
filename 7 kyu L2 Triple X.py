# 7 kyu
# L2: Triple X


def triple_x(s):
    return s[s.find('x'):s.find('x')+2] == 'xx'


print(triple_x(""), False)
print(triple_x("there's no XXX here"), False)
print(triple_x("abraxxxas"), True)
print(triple_x("xoxotrololololololoxxx"), False)
print(triple_x("soft kitty, warm kitty, xxxxx"), True)
print(triple_x("softx kitty, warm kitty, xxxxx"), False)
