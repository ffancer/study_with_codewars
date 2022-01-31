def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        cnt_bottle = 99
        while cnt_bottle != 1:
            print(f'{cnt_bottle} bottles of beer on the wall, {cnt_bottle} bottles of beer.')
            cnt_bottle -= 1
            print(f'Take one down and pass it around, {cnt_bottle} bottles of beer on the wall.')
print(HQ9('H'))
print(HQ9('Q'))
print(HQ9('9'))
print(HQ9('X'))
