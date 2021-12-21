def spacify(string):
    if len(string) == 1 or string == '':
        return string

    return ' '.join(i for i in string)



print(spacify("hello world"), "h e l l o   w o r l d")
print(spacify("12345"), "1 2 3 4 5")
print(spacify(""), "")
print(spacify("a"), "a")
print(spacify("Pippi"), "P i p p i")
