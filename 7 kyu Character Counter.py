def validate_word(word):
    # your code here
    pass


print(validate_word("abcabc"), True)
print(validate_word("Abcabc"), True)
print(validate_word("AbcabcC"), False)
print(validate_word("AbcCBa"), True)
print(validate_word("pippi"), False)
print(validate_word("?!?!?!"), True)
print(validate_word("abc123"), True)
print(validate_word("abcabcd"), False)
print(validate_word("abc!abc!"), True)
print(validate_word("abc:abc"), False)
