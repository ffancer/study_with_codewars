# Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
# The computer thinks out a number from 1 to n. The user has k attempts to guess. After each unsuccessful attempt, the computer reports less or more of the hidden number. At the end of the game, the text with the result (either “You guessed”, or “Attempts ended”).


from random import randrange

print('Угадайте число от 0 до 10/Guess a number from 0 to 10')
num_of_attempts = 1
num = randrange(0, 11, 1)
print(num)
print('Число попыток/Number of attempts - 3')

try:
    user_input = int(input('Напишите число/Write the number: '))

    # while type(user_input) != int or 0 > int(user_input) > 10:
    #
    #     user_input = input('Напишите число/Write the number: ')

    if user_input == num:
        print(f'Вы угадали число!/You guess a number! - {num}')
        print(f'Вам понадобилось {num_of_attempts} попыток/You need {num_of_attempts} tries')

    while user_input != num:

        print(f'Число попыток/Number of attempts - {num_of_attempts}')
        user_input = int(input('Напишите число/Write the number: '))
        num_of_attempts += 1

        if num_of_attempts == 3:
            print('Попытки кончились и вы не угадали число/Attempts ended and you did not guess the number')
            break
except:
    print(
        'Вы ввели не число, введите число от 0 до 10/You have not entered a number, please enter a number from 0 to 10')
    user_input = input('Напишите число/Write the number: ')
