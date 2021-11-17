# Дан текст. Найти сумму имеющихся в нем цифр.
# Given text. Find the sum of the digits in it.

def sum_digit(s):
    total = 0

    for i in s:
        if i.isdigit():
            total += int(i)

    return total


print(sum_digit('1ght57676g'))
print(sum_digit('1n'))
print(sum_digit('0vc0vg0mg5'))
print(sum_digit('123ghmnbd123'))
print(sum_digit('123456'))
print(sum_digit('mnbiu'))