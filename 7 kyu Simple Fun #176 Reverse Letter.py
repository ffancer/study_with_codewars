def reverse_letter(string):
    # first
    # s = ''
    #
    # for i in string:
    #     if 'z' >= i >= 'a':
    #         s += i
    #
    # return s[::-1]

    # second
    # s = [i for i in string if 'z' >= i >= 'a']
    # return ''.join(s)[::-1]

    # third
    #     return ''.join([i for i in string if 'z' >= i >= 'a'])[::-1]

    # fourth:
    return ''.join([i for i in string if i.isalpha()])[::-1]


print(reverse_letter("krishan"))

print(reverse_letter("ultr53o?n"))

print(reverse_letter("ab23c"))

print(reverse_letter("krish21an"))
