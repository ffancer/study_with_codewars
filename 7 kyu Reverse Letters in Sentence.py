def reverser(sentence):
    return ' '.join(i[::-1] for i in sentence.split(' '))

print(reverser("Hi mom"), "iH mom")
print(reverser("friendzone"), "enozdneirf")
print(reverser(" "), " ")
print(reverser("  "), "  ")
