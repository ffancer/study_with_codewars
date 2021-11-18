# Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
# The computer thinks out a number from 1 to n. The user has k attempts to guess. After each unsuccessful attempt, the computer reports less or more of the hidden number. At the end of the game, the text with the result (either “You guessed”, or “Attempts ended”).


from random import randint


num = randint(1, 101)
user_input = input('Ygadai 4islo: ')

while True:
    if user_input in ['q', 'quit']:
        print('Go next')
        break

    if user_input.isdigit():
        print('good')
        break
    else:
        user_input = input('vi vveli ne 4islo: ')
