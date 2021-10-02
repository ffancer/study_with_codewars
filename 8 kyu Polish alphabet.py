def correct_polish_letters(st):
    dct = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }
    s = ''

    for i in st:
        if i in dct:
            s += dct[i]
        else:
            s += i

    return s


print(correct_polish_letters("Jędrzej Błądziński"),"Jedrzej Bladzinski")
print(correct_polish_letters("Lech Wałęsa"),"Lech Walesa")
print(correct_polish_letters("Maria Skłodowska-Curie"),"Maria Sklodowska-Curie")