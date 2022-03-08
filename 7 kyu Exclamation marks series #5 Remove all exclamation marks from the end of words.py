# 7 kyu
# Exclamation marks series #5: Remove all exclamation marks from the end of words


def remove(s):
    return ' '.join(i.rstrip('!') for i in s.split())


print(remove('Hi!'), 'Hi')
print(remove('Hi!!!'), 'Hi')
print(remove('!Hi'), '!Hi')
print(remove('!Hi!'), '!Hi')
print(remove('Hi! Hi!'), 'Hi Hi')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi !hi')
