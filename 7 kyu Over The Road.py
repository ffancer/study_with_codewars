def over_the_road(address, n):
    return (2 * n + 1) - address


print(over_the_road(1, 3), 6)
print(over_the_road(3, 3), 4)
print(over_the_road(2, 3), 5)
print(over_the_road(3, 5), 8)
print(over_the_road(7, 11), 16)
print(over_the_road(23633656673, 310027696726), 596421736780)