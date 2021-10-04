def is_palindrome(string):
    if type(string) == int:
        string = str(string)
    i = 0
    j = len(string) - 1
    flag = True

    while i < j:
        if string[i] != string[j]:
            flag = False
        i += 1
        j -= 1

    return flag


print(is_palindrome("anna"), True)
print(is_palindrome("walter"), False)
print(is_palindrome(12321), True)
print(is_palindrome(123456), False)
