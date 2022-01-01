def spoonerize(words):
    a, b = words.split()
    return b[0] + a[1:] + ' ' + a[0] + b[1:]

print(spoonerize("nit picking"), "pit nicking")
print(spoonerize("wedding bells"), "bedding wells")
print(spoonerize("jelly beans"), "belly jeans")
print(spoonerize("pop corn"), "cop porn")
