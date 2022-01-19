# 7 kyu
# Who is the killer?


def killer(suspect_info, dead):
    for i, j in suspect_info.items():
        if all([i for i in dead]) in j:
            return i


print(
    killer({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']},
           ['Lucas', 'Bill']), 'James')
print(killer({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan')
