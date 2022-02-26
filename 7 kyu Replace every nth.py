def replace_nth(text, n, old, new):
    count = 0
    res = ""
    for c in text:
        if c == old:
            count += 1
            if count == n:
                res += new
                count = 0
                continue
        res += c
    return res


print(replace_nth("Vader said: No, I am your father!", 2, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 4, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 6, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 0, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", -2, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 1, 'i', 'y'))
print(replace_nth("Luke cries: Noooooooooooooooo!", 6, 'o', 'i'))