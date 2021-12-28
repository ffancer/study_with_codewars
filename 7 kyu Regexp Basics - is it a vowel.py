# 7 kyu
# Regexp Basics - is it a vowel?

def is_vowel(s):
    return s.lower() in ['a', 'e', 'i', 'o', 'u']


print(is_vowel(""), False)
print(is_vowel("a"), True)
print(is_vowel("E"), True)
print(is_vowel("ou"), False)
print(is_vowel("z"), False)
print(is_vowel("lol"), False)
