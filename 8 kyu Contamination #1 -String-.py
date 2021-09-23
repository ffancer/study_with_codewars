def contamination(text, char):
    return ''.join(list(i.replace(i, char) for i in text))


print(contamination("abc", "z"), "zzz")
print(contamination("", "z"), "")
print(contamination("abc", ""), "")
print(contamination("_3ebzgh4", "&"), "&&&&&&&&")
print(contamination("//case", " "), "      ")