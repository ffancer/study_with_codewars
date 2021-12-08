def capitalize(s, ind):
    lst = list(s)
    for i in ind:
        try:
            lst[i] = lst[i].upper()
        except IndexError:
            break
    return ''.join(lst)



print(capitalize("abcdef", [1, 2, 5]), 'aBCdeF')
print(capitalize("abcdef", [1, 2, 5, 100]), 'aBCdeF', )
print(capitalize("codewars", [1, 3, 5, 50]), 'cOdEwArs')
print(capitalize("abracadabra", [2, 6, 9, 10]), 'abRacaDabRA')
print(capitalize("codewarriors", [5]), 'codewArriors')
