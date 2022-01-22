def rgb(r, g, b):
    return f'{hex(r)[2:].upper()}{hex(g)[2:].upper()}{hex(b)[2:].upper()}'


print(rgb(0, 0, 0), "000000", "testing zero values")
print(rgb(1, 2, 3), "010203", "testing near zero values")
print(rgb(255, 255, 255), "FFFFFF", "testing max values")
print(rgb(254, 253, 252), "FEFDFC", "testing near max values")
print(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
