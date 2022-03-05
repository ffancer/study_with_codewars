# 7 kyu
# Exclamation marks series #3: Remove all exclamation marks from sentence except at the end


def remove(s):
    point = s.find('H')
    s = s[:point].replace('!', '') + s[point:]
    return s



print(remove('Hi!'), 'Hi!')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), 'Hi')
print(remove('!Hi!'), 'Hi!')
print(remove('Hi! Hi!'), 'Hi Hi!')
print(remove('Hi'), 'Hi')
