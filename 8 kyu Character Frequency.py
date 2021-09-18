def char_freq(message):
    return {i: message.count(i) for i in message}


print(char_freq("I like cats"), {'a': 1, ' ': 2, 'c': 1, 'e': 1, 'I': 1, 'k': 1, 'l': 1, 'i': 1, 's': 1, 't': 1})