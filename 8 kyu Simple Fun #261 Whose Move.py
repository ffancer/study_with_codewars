# 8 kyu
# Simple Fun #261: Whose Move

def whoseMove(lastPlayer, win):
    return lastPlayer if win else 'white' if lastPlayer == 'black' else 'black'


print(whoseMove('black', False), 'white')
print(whoseMove('white', False), 'black')
print(whoseMove('black', True), 'black')
print(whoseMove('white', True), 'white')
