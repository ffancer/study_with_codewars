def potatoes(p0, w0, p1):
    return (100 - p0) * w0 // (100 - p1)


print(potatoes(82, 127, 80), 114)
print(potatoes(93, 129, 91), 100)
