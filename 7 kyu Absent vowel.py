def absent_vowel(x):
    dct = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}

    for i, j in dct.items():
        print(i, j)


print(absent_vowel("John Doe hs seven red pples under his bsket"), 0)
print(absent_vowel("Bb Smith sent us six neatly arranged range bicycles"), 3)
