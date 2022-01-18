def even_chars(st):
    lst = []

    for i, j in enumerate(st, 1):
        if i % 2 == 0:
            lst.append(j)

    return "invalid string" if len(lst) < 3 or len(st) > 100 else lst


print(even_chars("a"), "invalid string")
print(even_chars("abcdefghijklm"), ["b", "d", "f", "h", "j", "l"])
print(even_chars("aBc_e9g*i-k$m"), ["B", "_", "9", "*", "-", "$"])
