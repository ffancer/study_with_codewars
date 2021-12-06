def has_unique_chars(string):
    i = 0

    while i != len(string)-1:
        if string[i] == string[i+1]:
            return False
        i += 1

    return True

print(has_unique_chars("abcdef"), True)
print(has_unique_chars("++-"), False)
print(has_unique_chars("  nAa"), False)
