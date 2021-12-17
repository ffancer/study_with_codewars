def outed(meet, boss):
    total = 0

    for i, j in meet.items():
        if boss == i:
            total += j * 2
        else:
            total += j

    return 'Get Out Now!' if total / len(meet) <= 5 else 'Nice Work Champ!'


print(outed(
    {'tim': 0, 'jim': 2, 'randy': 0, 'sandy': 7, 'andy': 0, 'katie': 5, 'laura': 1, 'saajid': 2, 'alex': 3,
     'john': 2, 'mr': 0}, 'laura'), 'Get Out Now!')
print(outed(
    {'tim': 1, 'jim': 3, 'randy': 9, 'sandy': 6, 'andy': 7, 'katie': 6, 'laura': 9, 'saajid': 9, 'alex': 9,
     'john': 9, 'mr': 8}, 'katie'), 'Nice Work Champ!')
print(outed(
    {'tim': 2, 'jim': 4, 'randy': 0, 'sandy': 5, 'andy': 8, 'katie': 6, 'laura': 2, 'saajid': 2, 'alex': 3,
     'john': 2, 'mr': 8}, 'john'), 'Get Out Now!')
