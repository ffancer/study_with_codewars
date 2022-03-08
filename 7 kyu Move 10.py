def move_ten(st):
    s = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'

    for i, j in enumerate(alph):
        # print(i, j)
        if j in st:
            s += alph[(i + 10) % len(alph)]

    return s


print(move_ten("testcase"), "docdmkco")
print(move_ten("codewars"), "mynogkbc")
print(move_ten("exampletesthere"), "ohkwzvodocdrobo")
print(move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov")
print(move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz")
print(move_ten("weneedanofficedog"), "goxoonkxyppsmonyq")
