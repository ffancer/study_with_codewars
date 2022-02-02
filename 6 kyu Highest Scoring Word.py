def high(x):

    def points_calc(s):
        total = 0
        for i in s:
            if i.isalpha():
                total += ord(i) - 96
        return total

    x = x.split()

    dct = {i: points_calc(i) for i in x}

    return sorted(dct.values(), reverse=True)[0]

print(high('man i need a taxi up to ubud'), 'taxi')
print(high('what time are we climbing up the volcano'), 'volcano')
print(high('take me to semynak'), 'semynak')
print(high('aa b'), 'aa')
print(high('b aa'), 'b')
print(high('bb d'), 'bb')
print(high('d bb'), 'd')
print(high("aaa b"), "aaa")
