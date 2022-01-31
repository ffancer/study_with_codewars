def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    if code == 'Q':
        return code
    if code == '9':
        lst = []
        next_string = ''
        for n in range(99, -1, -1):
            if n != 0:
                bottle_s = f'bottle{"s" if n > 1 else ""}'
                next_string = f'{n} {bottle_s} of beer on the wall, {n} {bottle_s} of beer.\nTake one down and pass it around, {n - 1 if n > 1 else "no more"} bottle{"s" if n - 1 != 1 else ""} of beer on the wall.'
            else:
                next_string = 'No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
            lst.append(next_string)
        return '\n'.join(lst)


print(HQ9('H'))
print(HQ9('Q'))
print(HQ9('9'))
print(HQ9('X'))
