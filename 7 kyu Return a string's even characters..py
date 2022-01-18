def even_chars(st):
    lst = []
    for i, j in enumerate(st, 1):
        # print(i, j)
        if i % 2 == 0:
            lst.append(j)
    return lst


print(even_chars("a"), "invalid string")
print(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
print(even_chars("aBc_e9g*i-k$m"), ["B", "_", "9", "*", "-", "$"])
