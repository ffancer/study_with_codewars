def remove_duplicate_words(s):
    # first:
    # lst = []
    # s = s.split()
    #
    # for i in s:
    #     if i not in lst:
    #         lst.append(i)
    #
    # return ' '.join(lst)

    # second:
    lst = []
    [lst.append(i) for i in s.split() if i not in lst]
    return ' '.join(lst)

print(remove_duplicate_words("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))  # "alpha beta gamma delta"
print(remove_duplicate_words("my cat is my cat fat"))  # "my cat is fat"