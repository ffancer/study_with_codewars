def rgb(r, g, b):
    def round_our_rgb(num):
        return min(255, max(num, 0))

    return round_our_rgb(r), round_our_rgb(b), round_our_rgb(g)


# return f'{hex(r)[2:].upper()}{hex(g)[2:].upper()}{hex(b)[2:].upper()}'

# return ("{:02X}" * 3).format(hex(r)[2:].upper(), hex(g)[2:].upper(), hex(b)[2:].upper())


print(rgb(0, 0, 0), "000000", "testing zero values")
print(rgb(1, 2, 3), "010203", "testing near zero values")
print(rgb(255, 255, 255), "FFFFFF", "testing max values")
print(rgb(254, 253, 252), "FEFDFC", "testing near max values")
print(rgb(-20, 275, 125), "00FF7D", "testing out of range values")
