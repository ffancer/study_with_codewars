def is_palindrome(string):
    if type(string) == int:
        string = str(string)
    return string == string[::-1]


print(is_palindrome("anna"), True)
print(is_palindrome("walter"), False)
print(is_palindrome(12321), True)
print(is_palindrome(123456), False)
