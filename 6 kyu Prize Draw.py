def rank(st, we, n):
    total = 0

    for i in n:
        total += ord(i)-96


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
print(rank("Lagon,Lily", [1, 5], 2), "Lagon")
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), "Not enough participants")
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participants")
