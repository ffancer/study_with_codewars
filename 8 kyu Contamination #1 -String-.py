def contamination(text, char):
    return char*len(text)


print(contamination("abc", "z"), "zzz")
print(contamination("", "z"), "")
print(contamination("abc", ""), "")
print(contamination("_3ebzgh4", "&"), "&&&&&&&&")
print(contamination("//case", " "), "      ")