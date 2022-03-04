def filter_even_length_words(words):
    lst = []

    for i in words:
        if len(i) % 2 == 0:
            lst.append(i)

    return lst


print(filter_even_length_words(["Hello", "World"]), [])
print(filter_even_length_words(["One", "Two", "Three", "Four"]), ["Four"])
