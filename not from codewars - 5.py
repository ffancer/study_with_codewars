# Компьютер загадывает число от 1 до n. У пользователя k попыток отгадать. После каждой неудачной попытки компьютер сообщает меньше или больше загаданное число. В конце игры текст с результатом (или “Вы угадали”, или “Попытки закончились”).
# The computer thinks out a number from 1 to n. The user has k attempts to guess. After each unsuccessful attempt, the computer reports less or more of the hidden number. At the end of the game, the text with the result (either “You guessed”, or “Attempts ended”).


from random import randint

print('Для выхода введите "выход", "в"/For quit enter "quit", "q"')
print('У вас 3 попытки/You have 3 attempts')
print()
num = randint(1, 101)
cnt_of_attempts = 2
print(f'answer - {num}')  # for debug
user_input = input('Напишите число/Write the number: ')

while True:
    if user_input in ['q', 'quit', 'выход', 'в'] or cnt_of_attempts == 0:
        print('GL next')
        break

    if user_input.isdigit():
        if user_input == str(num):
            print('Число угаданно!/Number guessed!')
            break
        else:
            print('Ваше число ' + ('меньше' if num > int(user_input) else 'больше') + ' чем задумал компьютер')
            print('Your number ' + ('less' if num > int(user_input) else 'greater') + ' than the computer intended')
            user_input = input('Введите число/Enter the number: ')
    else:
        user_input = input('Вы ввели не число/You entered not a number: ')

    cnt_of_attempts -= 1
