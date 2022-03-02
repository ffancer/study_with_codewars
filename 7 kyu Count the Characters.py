def count_char(*args):
    return args[0].lower().count(args[1].lower())


print(count_char("Hello there", "e"), 3)
print(count_char("Hello there", "t"), 1)
print(count_char("Hello there", "h"), 2)
print(count_char("Hello there", "L"), 2)
print(count_char("Hello there", " "), 1)