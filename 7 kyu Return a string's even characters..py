def even_chars(st):
    if len(st) > 100 or len(st) < 3:
        return "invalid string"

    lst = []

    for i,j in enumerate(st):
        if i % 2 != 0:
            lst.append(j)

    return lst


print(even_chars("a"), "invalid string")
print(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
print(even_chars("aBc_e9g*i-k$m"), ["B", "_", "9", "*", "-", "$"])
print(even_chars("1234567890" * 11), "invalid string")
