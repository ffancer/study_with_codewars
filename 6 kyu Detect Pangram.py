import string

def is_pangram(s):
    ascii_s = string.ascii_lowercase
    for i in s:
        if i in ascii_s:
            ascii_s = ascii_s.replace(i, '')

    return ascii_s == ''


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)
print(is_pangram('aaaabbbbbffdfdfdfd'), False)