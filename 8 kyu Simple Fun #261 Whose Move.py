# 8 kyu
# Simple Fun #261: Whose Move
def whoseMove(lastPlayer, win):
    answer = ''

    if lastPlayer == 'black' and win is False:
        answer = 'white'
    elif lastPlayer == 'white' and win is False:
        answer = 'black'
    elif lastPlayer == 'black' and win is True:
        answer = 'black'
    elif lastPlayer == 'white' and win is True:
        answer = 'white'

    return answer


print(whoseMove('black', False), 'white')
print(whoseMove('white', False), 'black')
print(whoseMove('black', True), 'black')
print(whoseMove('white', True), 'white')
