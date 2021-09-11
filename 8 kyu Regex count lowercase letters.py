def lowercase_count(strng):
    return sum([i.count(i) for i in strng if i.islower()])


print(lowercase_count("abc"), 3)
print(lowercase_count("abcABC123"), 3)
print(lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 3)
print(lowercase_count(""), 0)
print(lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~"), 0)
print(lowercase_count("abcdefghijklmnopqrstuvwxyz"), 26)