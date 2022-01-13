letters = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie",
    "D": "Delta", "E": "Echo", "F": "Foxtrot",
    "G": "Golf", "H": "Hotel", "I": "India",
    "J": "Juliett", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu"
}


def nato(word):
    s = ''

    for i in word:
        # if i in letters.keys():
        #     s += letters[i]
        print(letters.get(i.upper()))
    return s

print(nato("babble"), "Bravo Alpha Bravo Bravo Lima Echo")
