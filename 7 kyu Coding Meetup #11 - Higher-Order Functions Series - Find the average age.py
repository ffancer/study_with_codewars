def get_average(lst):
    return sum(i['age'] for i in lst) // len(lst)


list1 = [
    {'firstName': 'Maria', 'lastName': 'Y.', 'country': 'Cyprus', 'continent': 'Europe', 'age': 30, 'language': 'Java'},
    {'firstName': 'Victoria', 'lastName': 'T.', 'country': 'Puerto Rico', 'continent': 'Americas', 'age': 70,
     'language': 'Python'},
]
print(get_average(list1), 50)

list2 = [
    {'firstName': 'Noa', 'lastName': 'A.', 'country': 'Israel', 'continent': 'Asia', 'age': 20, 'language': 'Ruby'},
    {'firstName': 'Andrei', 'lastName': 'E.', 'country': 'Romania', 'continent': 'Europe', 'age': 21, 'language': 'C'},
]
print(get_average(list2), 20)