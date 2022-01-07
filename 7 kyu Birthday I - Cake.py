def cake(candles, debris):
    total = 0

    for i,j in enumerate(debris):
        # total += ord(i)-96
        print(i, j)

    # return 'Fire!' if candles * 0.7 < total else 'That was close!'
    # return total


print(cake(900, 'abcdef'), 'That was close!')
print(cake(56, 'ifkhchlhfd'), 'Fire!')
print(cake(256, 'aaaaaddddr'), 'Fire!')
print(cake(333, 'jfmgklfhglbe'), 'Fire!')
print(cake(12, 'jaam'), 'Fire!')
