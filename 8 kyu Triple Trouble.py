def triple_trouble(one, two, three):
    s = ''

    for i in range(len(one)):
        s += f'{one[i]}{two[i]}{three[i]}'

    return s



print(triple_trouble("aaa", "bbb", "ccc"), "abcabcabc")
print(triple_trouble("aaaaaa", "bbbbbb", "cccccc"), "abcabcabcabcabcabc")
print(triple_trouble("burn", "reds", "roll"), "brrueordlnsl")
print(triple_trouble("Bm", "aa", "tn"), "Batman")
print(triple_trouble("LLh", "euo", "xtr"), "LexLuthor")