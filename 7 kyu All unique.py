def has_unique_chars(string):
    for i in range(len(string)):
        if string[i] == string[i + 1]:
            return False
        return True


print(has_unique_chars("abcdef"), True)
print(has_unique_chars("++-"), False)
print(has_unique_chars("  nAa"), False)
