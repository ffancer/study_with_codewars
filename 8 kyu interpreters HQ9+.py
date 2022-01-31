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

        print('1 bottle of beer on the wall, 1 bottle of beer.')
        print('Take one down and pass it around, no more bottles of beer on the wall.')
        print('No more bottles of beer on the wall, no more bottles of beer.')
        print('Go to the store and buy some more, 99 bottles of beer on the wall.')
print(HQ9('H'))
print(HQ9('Q'))
print(HQ9('9'))
print(HQ9('X'))
