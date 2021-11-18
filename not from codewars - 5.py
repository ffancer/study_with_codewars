# Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
# The computer thinks out a number from 1 to n. The user has k attempts to guess. After each unsuccessful attempt, the computer reports less or more of the hidden number. At the end of the game, the text with the result (either “You guessed”, or “Attempts ended”).


from random import randrange

print('Угадайте число от 1 до 100/Guess a number from 1 to 100')
num_of_attempts = 2
num = randrange(1, 101, 1)
print(num)
print('У Вас 3 попытки/You have 3 attempts')

try:
    user_input = int(input('Напишите число/Write the number: '))
    if user_input == num:
        print(f'Вы угадали число!/You guess a number! - {num}')
        print(f'Вам понадобилось {num_of_attempts} попыток/You need {num_of_attempts} tries')

    while user_input != num:
        print(f'Число попыток/Number of attempts - {num_of_attempts}')

        if num > user_input:
            print('Загаданное число больше Вашего/The guessed number is greater than yours')
        elif num < user_input:
            print('Загаданное число меньше Вашего/The guessed number is less than yours')

        user_input = int(input('Напишите число/Write the number: '))
        num_of_attempts -= 1

        if num_of_attempts == 0:
            print('Попытки кончились и вы не угадали число/Attempts ended and you did not guess the number')
            break
except:
    print(
        'Вы ввели не число, введите число от 0 до 10/You have not entered a number, please enter a number from 0 to 10')
    user_input = input('Напишите число/Write the number: ')


    # постараться сделать так что бы при вводе знаков и букв просило вводить цифру
