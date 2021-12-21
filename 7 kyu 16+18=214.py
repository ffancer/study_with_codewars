def add(num1, num2):
    answer = ''

    last_digit1 = num1 % 10
    last_digit2 = num2 % 10

    while len(str(num1)) != len(str(num2)):
        answer += str(last_digit1 + last_digit2)
        last_digit1 = str(num1)[:-1] % 10
        last_digit2 = str(num2)[:-1] % 10
    return answer


print(add(2, 11), 13)
print(add(0, 1), 1)
print(add(0, 0), 0)
print(add(16, 18), 214)
print(add(26, 39), 515)
print(add(122, 81), 1103)
