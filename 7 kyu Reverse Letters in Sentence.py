def reverser(sentence):
    s = ''
    splt = sentence.split()
    for i in splt:
        s += str(i)[::-1] + ' '

    if sentence[0] == ' ':
        return ' ' + s
    if sentence[-1] == ' ':
        return s + ' '
    if sentence[0] == ' ' and sentence[-1] == ' ':
        return s.strip()


print(reverser("Hi mom"), "iH mom")
print(reverser("friendzone"), "enozdneirf")
print(reverser(" "), " ")
print(reverser("  "), "  ")
