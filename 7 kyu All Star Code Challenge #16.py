def no_repeat(string):
    for i in string:
        if string.count(i) == 1:
            return i


print(no_repeat("aabbccdde"), "e")
print(no_repeat("wxyz"), "w")
print(no_repeat("testing"), "e")
print(no_repeat("codewars"), "c")
print(no_repeat("Testing"), "T")
