# 7 kyu
# L2: Triple X


# best practice 1
def triple_x(s):
    pos = s.find('x')
    return s[pos:pos + 3] == 'xxx'

# best practice 2
triple_x = lambda s: s.find('x') == s.find('xxx') > -1

# print(triple_x(""), False)
# print(triple_x("there's no XXX here"), False)
print(triple_x("abraxxxas"), True)
print(triple_x("xoxotrololololololoxxx"), False)
print(triple_x("soft kitty, warm kitty, xxxxx"), True)
print(triple_x("softx kitty, warm kitty, xxxxx"), False)
