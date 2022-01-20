import string

def is_pangram(s):
    lst = [1] * 26
    lst_s = []
    for i in s:
        lst_s.append(s.count(i))


    return lst_s


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)