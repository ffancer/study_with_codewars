def rps(p1, p2):
    answer = ""

    if p1 == 'rock' and p2 == 'scissors' or p1 == 'paper' and p2 == 'rock' or p1 == 'scissors' and p2 == 'paper':
        answer = 'Player 1 won!'
    elif p1 == 'scissors' and p2 == 'rock' or p1 == 'rock' and p2 == 'paper' or p1 == 'paper' and p2 == 'scissors':
        answer = "Player 2 won!"
    else:
        answer = 'Draw!'

    return answer




print(rps('rock', 'scissors'), "Player 1 won!")
print(rps('scissors', 'rock'), "Player 2 won!")
print(rps('rock', 'rock'), 'Draw!')