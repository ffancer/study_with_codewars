def validBraces(string):
    lst = ['(}', '(]', '[)', '[}', '{)', '{]']

    for i in lst:
        if i in string:
            return False
    return True


print(validBraces("()"), True)
print(validBraces("[(])"), False)
