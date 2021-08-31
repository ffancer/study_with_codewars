def replace_exclamation(s):
    s2 = ''

    for i in s:
        if i in 'aeiouAEIOU':
            s2 += '!'
        else:
            s2 += i

    return s2


print(replace_exclamation("Hi!"), "H!!")
print(replace_exclamation("!Hi! Hi!"), "!H!! H!!")
print(replace_exclamation("aeiou"), "!!!!!")
print(replace_exclamation("ABCDE"), "!BCD!")
