def add(num1, num2):
    num1, num2 = str(num1), str(num2)
    answer = ''

    if len(num1) > len(num2):
        num2 = num2.zfill(len(num1) - len(num2)+len(num2))
    if len(num2) > len(num1):
        num1 = num1.zfill(len(num2) - len(num1)+len(num1))

    while len(num1) != 0:
        answer += str(int(num1[0]) + int(num2[0]))
        num1 = num1[1:]
        num2 = num2[1:]

    return int(answer)

print(add(2, 11), 13)
print(add(0, 1), 1)
print(add(0, 0), 0)
print(add(16, 18), 214)
print(add(26, 39), 515)
print(add(122, 81), 1103)
