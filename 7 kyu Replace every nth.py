def replace_nth(text, n, old, new):
    return text.replace(old, new, n)


print(replace_nth("Vader said: No, I am your father!", 2, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 4, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 6, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 0, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", -2, 'a', 'o'))
print(replace_nth("Vader said: No, I am your father!", 1, 'i', 'y'))
print(replace_nth("Luke cries: Noooooooooooooooo!", 6, 'o', 'i'))