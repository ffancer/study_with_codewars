def spoonerize(words):
    a, b = words.split()[0][0], words.split()[-1][0]
    return b + words.split()[0][1:] + ' ' + a + words.split()[-1][1:]

print(spoonerize("nit picking"), "pit nicking")
print(spoonerize("wedding bells"), "bedding wells")
print(spoonerize("jelly beans"), "belly jeans")
print(spoonerize("pop corn"), "cop porn")
