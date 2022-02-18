class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        return n == self.number


guesser = Guesser(10, 2)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
print(guesser.guess(10), True)

# test.it('Wrong guess should return false')
guesser = Guesser(10, 2)
guesser.guess(1)
print(guesser.guess(1), False)

# test.it('Lives ran out should throw')
guesser = Guesser(10, 2)
guesser.guess(1)
guesser.guess(2)

print('Expect error: "Omae wa mo shindeiru"', lambda: guesser.guess(10))