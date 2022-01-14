def seqlist(first, c, l):
    return range(first, first + l * c, c)


print(seqlist(0, 1, 20), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
print(seqlist(0, 3, 58))
print(seqlist(0, -5, -96))
