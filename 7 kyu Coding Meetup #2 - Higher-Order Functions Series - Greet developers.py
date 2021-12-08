def greet_developers(lst):
    arr = []

    for i in lst:
        temp = i
        temp['greeting'] = f'Hi {i["firstName"]}, what do you like the most about {i["language"]}?'
        arr.append(temp)

    return arr


print(greet_developers([
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
     'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
     'language': 'Python'},
    {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
     'language': 'Ruby'}
]))
