def count_languages(lst):
    arr = []

    for i in lst:
        arr.append(i['language'])

    return dict(zip(arr, [arr.count(i) for i in arr]))


list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
     'language': 'C'},
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52,
     'language': 'JavaScript'},
    {'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29,
     'language': 'Ruby'},
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81,
     'language': 'C'},
]
answer = {'C': 2, 'JavaScript': 1, 'Ruby': 1}
print(count_languages(list1), answer)
