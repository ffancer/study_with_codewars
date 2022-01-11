def count_arara(n):
    anane = 'anane'  # it's 1
    adak = 'adak'  # it's 2
    s = ''

    while n != 0:
        if n >= 2:
            n -= 2
            s += adak + ' '
        else:
            n -= 1
            s += anane + ' '

    return s[:-1]


print(count_arara(1), "anane")
print(count_arara(2), "adak")
print(count_arara(3), "adak anane")
print(count_arara(9), "adak adak adak adak anane")
