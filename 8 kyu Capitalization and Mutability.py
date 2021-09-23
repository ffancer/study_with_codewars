def capitalize_word(word):
    return "".join(char.upper() for char in word)


print(capitalize_word('word'), 'Word')
print(capitalize_word('i'), 'I')
print(capitalize_word('glasswear'), 'Glasswear')