def order_food(lst):
    ans = []

    for i in lst:
        ans.append(i['meal'])

    dct = {i: ans.count(i) for i in ans}

    return dct



list1 = [
    {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C',
     'meal': 'vegetarian'},
    {'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52,
     'language': 'JavaScript', 'meal': 'standard'},
    {'firstName': 'Ramona', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29,
     'language': 'Ruby', 'meal': 'vegan'},
    {'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C',
     'meal': 'vegetarian'},
]
# answer = {'vegetarian': 2, 'standard': 1, 'vegan': 1}
print(order_food(list1))