def contamination(text, char):
    s = ''

    for i in text:
        s += i.replace(i, char)

    return s


print(contamination("abc", "z"), "zzz")
print(contamination("", "z"), "")
print(contamination("abc", ""), "")
print(contamination("_3ebzgh4", "&"), "&&&&&&&&")
print(contamination("//case", " "), "      ")