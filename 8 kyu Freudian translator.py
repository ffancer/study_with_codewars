def to_freud(sentence):
    return ' '.join(['sex' for _ in sentence.split()])



print(to_freud("test"), "sex")
print(to_freud("sexy sex"), "sex sex")
print(to_freud("This is a test"), "sex sex sex sex")
print(to_freud("This is a longer test"), "sex sex sex sex sex")
print(to_freud("You're becoming a true freudian expert"), "sex sex sex sex sex sex")