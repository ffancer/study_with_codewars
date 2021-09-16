# 8 kyu Is it a palindrome?
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


print(is_palindrome('a'), True)
print(is_palindrome('aba'), True)
print(is_palindrome('Abba'), True)
print(is_palindrome('malam'), True)
print(is_palindrome('walter'), False)
print(is_palindrome('kodok'), True)
print(is_palindrome('Kasue'), False)