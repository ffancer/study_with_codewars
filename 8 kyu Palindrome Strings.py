def is_palindrome(string):
    return str(string).lower() == str(string).lower()[::-1]


print(is_palindrome("anna"), True)
print(is_palindrome("walter"), False)
print(is_palindrome(12321), True)
print(is_palindrome(123456), False)
