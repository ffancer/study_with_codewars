import string

def is_pangram(s):
    ascii_s = string.ascii_lowercase
    return ascii_s


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)