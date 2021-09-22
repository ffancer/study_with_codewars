def define_suit(card):
    if card.endswith('C'):
        return 'clubs'
    elif card.endswith('S'):
        return 'spades'
    elif card.endswith('D'):
        return 'diamonds'
    elif card.endswith('H'):
        return 'hearts'


print(define_suit('3C'), 'clubs')
print(define_suit('QS'), 'spades')
print(define_suit('9D'), 'diamonds')
print(define_suit('JH'), 'hearts')
