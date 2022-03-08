# 7 kyu
# Exclamation marks series #5: Remove all exclamation marks from the end of words


def remove(s):
    s = s.split()
    return s[-1].rstrip('!')


print(remove('Hi!'), 'Hi')
print(remove('Hi!!!'), 'Hi')
print(remove('!Hi'), '!Hi')
print(remove('!Hi!'), '!Hi')
print(remove('Hi! Hi!'), 'Hi Hi')
print(remove('!!!Hi !!hi!!! !hi'), '!!!Hi !!hi !hi')
