# 7 kyu
# Exclamation marks series #3: Remove all exclamation marks from sentence except at the end


def remove(s):
    ans = ''
    flag = False

    for i in s[::-1]:
        if i == '!':
            if not flag:
                ans += i
        else:
            if not flag and i.isalpha():
                flag = True
            ans += i

    return ans[::-1]


print(remove('Hi!'), 'Hi!')
print(remove('Hi!!!'), 'Hi!!!')
print(remove('!Hi'), 'Hi')
print(remove('!Hi!'), 'Hi!')
print(remove('Hi! Hi!'), 'Hi Hi!')
print(remove('Hi'), 'Hi')
