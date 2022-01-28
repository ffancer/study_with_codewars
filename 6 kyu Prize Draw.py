def rank(st, we, n):
    if st == '':
        return "No participants"

    participants = {i : 0 for i in st.split(',')}

    return participants
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 4), "Benjamin")
print(rank("Lagon,Lily", [1, 5], 2), "Lagon")
print(rank("Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin", [4, 2, 1, 4, 3, 1, 2], 8), "Not enough participants")
print(rank("", [4, 2, 1, 4, 3, 1, 2], 6), "No participants")
