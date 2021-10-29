def word_pattern(word):
    word = word.lower()
    j = 0
    dct = {}
    lst = []

    for i in word:
        if i not in dct:
            dct[i] = str(j)
            j += 1

    for i in word:
        lst.append(dct[i])

    return '.'.join(lst)


print(word_pattern("hello"), "0.1.2.2.3"),
print(word_pattern("heLlo"), "0.1.2.2.3"),
print(word_pattern("helLo"), "0.1.2.2.3"),
print(word_pattern("Hippopotomonstrosesquippedaliophobia"),
      "0.1.2.2.3.2.3.4.3.5.3.6.7.4.8.3.7.9.7.10.11.1.2.2.9.12.13.14.1.3.2.0.3.15.1.13")
