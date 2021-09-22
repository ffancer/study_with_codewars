def define_suit(card):
    return {'C': 'clubs', 'S': 'spades', 'D': 'diamonds', 'H': 'hearts'}[card[-1]]


print(define_suit('3C'), 'clubs')
print(define_suit('QS'), 'spades')
print(define_suit('9D'), 'diamonds')
print(define_suit('JH'), 'hearts')
