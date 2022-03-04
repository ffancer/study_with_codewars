def string_merge(string1, string2, letter):
    # return string1.find(letter), string2.find(letter)
    return string1[:string1.find(letter)], string2[string2.find(letter):]

print(string_merge("hello", "world", "l"), "held")
print(string_merge("coding", "anywhere", "n"), "codinywhere")
print(string_merge("jason", "samson", "s"), "jasamson")
print(string_merge("wonderful", "people", "e"), "wondeople")