def to_freud(sentence):
    s = ''
    sentence = sentence.split()

    for i in range(len(sentence)):
        s += 'sex '

    return s[:-1]


print(to_freud("test"), "sex")
print(to_freud("sexy sex"), "sex sex")
print(to_freud("This is a test"), "sex sex sex sex")
print(to_freud("This is a longer test"), "sex sex sex sex sex")
print(to_freud("You're becoming a true freudian expert"), "sex sex sex sex sex sex")
