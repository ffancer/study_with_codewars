def is_flush(cards):
    return cards[0][1] == cards[1][1] == cards[2][1] == cards[3][1] == cards[4][1]

print(is_flush(["AS", "3S", "9S", "KS", "4S"]), True)
print(is_flush(["AD", "4S", "7H", "KC", "5S"]), False)
print(is_flush(["AD", "4S", "10H", "KC", "5S"]), False)
print(is_flush(["QD", "4D", "10D", "KD", "5D"]), True)