def word_search(query, seq):
    lst = []

    for i in seq:
        if query in i.lower():
            lst.append(i)

    return lst


print(word_search("ab", ["za", "ab", "abc", "zab", "zbc"]), ["ab", "abc", "zab"])
