def double_char(s):
    # first:
    # s2 = ''
    #
    # for i in s:
    #     s2 += i * 2
    #
    # return s2

    # second:
    return ''.join([i*2 for i in s])


print(double_char("String"))
print(double_char("Hello World"))
print(double_char("1234!_ "))