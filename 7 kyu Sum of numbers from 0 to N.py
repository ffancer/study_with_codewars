def show_sequence(n):
    if n == 0:
        return '0=0'
    elif n < 0:
        return str(n) + '<0'

    s = ''
    total = 0

    for i in range(n+1):
        s += str(i) + '+'
        total += i

    return s[:-1] + ' = ' + str(total)


print((show_sequence(6)))  # "0+1+2+3+4+5+6 = 21"
print((show_sequence(7)))  # "0+1+2+3+4+5+6+7 = 28"
print((show_sequence(0)))
print((show_sequence(-1)))
print((show_sequence(-10)))
