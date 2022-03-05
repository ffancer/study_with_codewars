# 7 kyu
# Exclamation marks series #3: Remove all exclamation marks from sentence except at the end


def remove(s):
    ans = ''
    i = 1
    while s:
        if s[i-1] != '!' or s[i+1] != '!':
            ans += s[i]

    return ans


print(remove('Hi!'), 'Hi!')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), 'Hi')
print(remove('!Hi!'), 'Hi!')
print(remove('Hi! Hi!'), 'Hi Hi!')
print(remove('Hi'), 'Hi')
