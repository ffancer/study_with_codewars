def filter_even_length_words(words):
    return [i for i in words if len(i) % 2 == 0]


print(filter_even_length_words(["Hello", "World"]), [])
print(filter_even_length_words(["One", "Two", "Three", "Four"]), ["Four"])
