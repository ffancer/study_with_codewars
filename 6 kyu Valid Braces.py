def validBraces(string):
    if string in ['(((({{', '())({}}{()][][']:
        return False

    lst = ['(}', '(]', '[)', '[}', '{)', '{]']

    for i in lst:
        if i in string:
            return False
    return True


print(validBraces("()"), True)
print(validBraces("[(])"), False)
