def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')
print(high('aa b'), 'aa')
print(high('b aa'), 'b')
print(high('bb d'), 'bb')
print(high('d bb'), 'd')
print(high("aaa b"), "aaa")
