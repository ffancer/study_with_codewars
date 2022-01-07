def cake(candles, debris):
    if candles == 0:
        return 'That was close!'

    total = 0

    for i,j in enumerate(debris):
        if i % 2 != 0:
            total += ord(j)-96
        else:
            total += ord(j)

    return 'Fire!' if candles * 0.7 < total else 'That was close!'


print(cake(900, 'abcdef'), 'That was close!')
print(cake(56, 'ifkhchlhfd'), 'Fire!')
print(cake(256, 'aaaaaddddr'), 'Fire!')
print(cake(333, 'jfmgklfhglbe'), 'Fire!')
print(cake(12, 'jaam'), 'Fire!')
