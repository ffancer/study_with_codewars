def last(x):
    lst = x.split(' ')

    def last_letter(lst):
        return lst[-1]

    lst.sort(key=last_letter)
    return lst


print(last("man i need a taxi up to ubud"), ["a", "need", "ubud", "i", "taxi", "man", "to", "up"])
print(last("what time are we climbing up the volcano"),
      ["time", "are", "we", "the", "climbing", "volcano", "up", "what"])
print(last("take me to semynak"), ["take", "me", "semynak", "to"])
print(last("massage yes massage yes massage"), ["massage", "massage", "massage", "yes", "yes"])
print(last("take bintang and a dance please"), ["a", "and", "take", "dance", "please", "bintang"])
