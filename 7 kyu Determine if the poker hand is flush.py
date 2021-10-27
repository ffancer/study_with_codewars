def is_flush(cards):
    cards = ''.join(cards)
    return cards.count('H') == 5 or cards.count('C') == 5 or cards.count('D') == 5 or cards.count('S') == 5


print(is_flush(["AS", "3S", "9S", "KS", "4S"]), True)
print(is_flush(["AD", "4S", "7H", "KC", "5S"]), False)
print(is_flush(["AD", "4S", "10H", "KC", "5S"]), False)
print(is_flush(["QD", "4D", "10D", "KD", "5D"]), True)
