def remove_duplicate_words(s):
    lst = []
    s = s.split()

    for i in s:
        if i not in lst:
            lst.append(i)

    return ' '.join(lst)


print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))  # "alpha beta gamma delta"
print(remove_duplicate_words("my cat is my cat fat"))  # "my cat is fat"