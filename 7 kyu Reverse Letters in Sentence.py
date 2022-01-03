def reverser(sentence):
    lst = []
    for i in sentence.split(' '):
        lst.append(i)
    return lst

print(reverser("Hi mom"), "iH mom")
print(reverser("friendzone"), "enozdneirf")
print(reverser(" "), " ")
print(reverser("  "), "  ")
