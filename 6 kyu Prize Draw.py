from operator import itemgetter


def rank(st, we, n):
    if st == '':
        return "No participants"

    participants = {i: 0 for i in st.split(',')}

    if n > len(participants):
        return "Not enough participants"

    for i, j in enumerate(participants):
        total = len(j)
        for k in j:
            total += ord(k.lower()) - 96
        participants[j] = total * we[i]

    sorted_by_name = sorted(participants.items(), key=itemgetter(0))
    sorted_by_value = sorted(sorted_by_name, key=itemgetter(1), reverse=True)

    return list(sorted_by_value)[n - 1]


print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
print(rank("Lagon,Lily", [1, 5], 2), "Lagon")
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), "Not enough participants")
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participants")
