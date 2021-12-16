# 7 kyu
# Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?


def is_ruby_coming(lst):
    # your code here
    pass


list1 = [
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
     'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
     'language': 'Python'},
    {'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
     'language': 'Ruby'}
]
print(is_ruby_coming(list1), True)

list2 = [
    {'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
     'language': 'Java'},
    {'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
     'language': 'Python'}
]
print(is_ruby_coming(list2), False)