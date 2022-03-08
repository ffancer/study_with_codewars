def move_ten(st):
    s = ''

    for i in st:
        if i:
            s += chr((ord(i) + 10 - 97) % 26 + 65)
        else:
            s += chr((ord(i) + 10 - 65) % 26 + 97)

    return s.lower()


print(move_ten("testcase"), "docdmkco")
print(move_ten("codewars"), "mynogkbc")
print(move_ten("exampletesthere"), "ohkwzvodocdrobo")
print(move_ten("returnofthespacecamel"), "bodebxypdroczkmomkwov")
print(move_ten("bringonthebootcamp"), "lbsxqyxdrolyydmkwz")
print(move_ten("weneedanofficedog"), "goxoonkxyppsmonyq")
