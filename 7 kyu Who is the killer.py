# 7 kyu
# Who is the killer?


def killer(suspect_info, dead):
    for i,j in suspect_info.items():
        # print(i, j)
        for k in dead:
            if k in j:
                return i


print(
    killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']},
           ['Lucas', 'Bill']), 'James')
print(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')
