def capitalize(s):
    lst = []
    s2 = ''

    for i in range(len(s)):
        if i % 2 == 0:
            s2 += s[i].capitalize()
        else:
            s2 += s[i].lower()

    lst.append(s2)
    s2 = ''

    for i in range(len(s)):
        if i % 2 == 0:
            s2 += s[i].lower()
        else:
            s2 += s[i].capitalize()

    lst.append(s2)

    return lst

print(capitalize("abcdef"))
print(capitalize("codewars"))
print(capitalize("abracadabra"))
print(capitalize("codewarriors"))