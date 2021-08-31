def replace_exclamation(s):
    return ''.join(['!' if i in 'aeiouAEIOU' else i for i in s])


print(replace_exclamation("Hi!"), "H!!")
print(replace_exclamation("!Hi! Hi!"), "!H!! H!!")
print(replace_exclamation("aeiou"), "!!!!!")
print(replace_exclamation("ABCDE"), "!BCD!")
