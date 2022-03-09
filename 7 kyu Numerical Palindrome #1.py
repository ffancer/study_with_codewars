def palindrome(num):
    if str(num)[0].isalpha() or str(num)[0] == '-' or type(num) == str:
        return "Not valid"
    return str(num) == str(num)[::-1]


print(palindrome(1221), True)
print(palindrome(123322), False)
print(palindrome("ACCDDCCA"), "Not valid")
print(palindrome("1221"), "Not valid")
print(palindrome(-450), "Not valid")
