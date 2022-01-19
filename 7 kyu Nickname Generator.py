def nickname_generator(name):
    if len(name) < 4:
        return "Error: Name too short"
    # if name[3] in ['a', 'e', 'i', 'o', 'u']:  #'aeiou'
    #     return name[:3]
    return name[:3]


print(nickname_generator("Jimmy"), "Jim")
print(nickname_generator("Samantha"), "Sam")
print(nickname_generator("Sam"), "Error: Name too short")
print(nickname_generator("Kayne"), "Kay", "'y' is not a vowel")
print(nickname_generator("Melissa"), "Mel")
print(nickname_generator("James"), "Jam")
