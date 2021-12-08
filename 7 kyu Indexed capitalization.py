def capitalize(s, ind):
    s1 = ''
    for i in ind:
        if s[i].islower():
            s1 += s[i].upper()
        else:
            s1 += s[i]
    return s1



print(capitalize("abcdef", [1, 2, 5]), 'aBCdeF')
print(capitalize("abcdef", [1, 2, 5, 100]), 'aBCdeF', )
print(capitalize("codewars", [1, 3, 5, 50]), 'cOdEwArs')
print(capitalize("abracadabra", [2, 6, 9, 10]), 'abRacaDabRA')
print(capitalize("codewarriors", [5]), 'codewArriors')
