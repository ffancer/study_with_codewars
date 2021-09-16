# 8 kyu Is it a palindrome?
def is_palindrome(s):
    i = 0
    j = len(s) - 1
    flag = True

    while i < j:
        if s[i] != s[j]:
            flag = False
        i += 1
        j -= 1

    return flag


print(is_palindrome('a'), True)
print(is_palindrome('aba'), True)
print(is_palindrome('Abba'), True)
print(is_palindrome('malam'), True)
print(is_palindrome('walter'), False)
print(is_palindrome('kodok'), True)
print(is_palindrome('Kasue'), False)