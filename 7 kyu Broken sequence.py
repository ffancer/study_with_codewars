def find_missing_number(sequence):
    if sequence == '':
        return 0

    for i in sequence.split():
        if not i.isdigit():
            return 1

    for i, j in zip(sorted(list(map(int, sequence.split()))), range(1, len(sequence) + 1)):
        if i != j:
            return j
    return 0

print(find_missing_number("1 2 3 5"), 4, "It must work for missing middle terms")
print(find_missing_number("1 5"), 2, "It must work for missing more than one element")
print(find_missing_number(""), 0, "It must return 0 for an empty sequence")
print(find_missing_number("1 2 3 4 5"), 0, "It must return 0 if no number is missing")
print(find_missing_number("2 3 4 5"), 1, "It must return 1 for a sequence missing the first element")
print(find_missing_number("2 6 4 5 3"), 1, "It must work for a shuffled input")
print(find_missing_number("_______"), 1, "It must return 1 for an invalid sequence")
print(find_missing_number("2 1 4 3 a"), 1, "It must return 1 for an invalid sequence")
print(find_missing_number(
    "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 91 92 93 94 95 96 97 98 99 100 101 102"),
    90, "It must return 90")