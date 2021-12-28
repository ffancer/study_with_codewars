# 7 kyu
# Regexp Basics - is it a vowel?

def is_vowel(s):
    if s == '' or len(s) != 1:
        return False

    vowels = ['a', 'e', 'i', 'o', 'u']

    for i in s.lower():
        if i in vowels:
            return True
    return False


print(is_vowel(""), False)
print(is_vowel("a"), True)
print(is_vowel("E"), True)
print(is_vowel("ou"), False)
print(is_vowel("z"), False)
print(is_vowel("lol"), False)
